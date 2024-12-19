from django.shortcuts import render, get_object_or_404, redirect
from .models import Jewelry, Cart, CartItem, Ring, Earring, Pendant, Bracelet, Watch, Charm
from django.contrib import messages
from django.views.decorators.http import require_POST
from .forms import PendantForm

@require_POST
def add_to_cart(request, jewelry_id):
    jewelry = get_object_or_404(Jewelry, id=jewelry_id)
    cart = request.session.get('cart', {})
    if str(jewelry_id) not in cart:
        cart[str(jewelry_id)] = {
            'name': jewelry.name,
            'price': str(jewelry.price),
            'quantity': 1,
            'image': jewelry.image.url
        }
    else:
        cart[str(jewelry_id)]['quantity'] += 1
    request.session['cart'] = cart

    messages.success(request, 'Товар добавлен в корзину.')
    return redirect('cart_detail')

def cart_detail(request):
    cart = request.session.get('cart', {})
    return render(request, 'shop/cart_detail.html', {'cart': cart})


@require_POST
def remove_from_cart(request, item_id):
    cart = request.session.get('cart', {})
    if str(item_id) in cart:
        del cart[str(item_id)]
        request.session['cart'] = cart
        messages.success(request, 'Товар удален из корзины.')
    return redirect('cart_detail')

def remove_from_session_cart(request, jewelry_id):
    cart = request.session.get('cart', {})
    if str(jewelry_id) in cart:
        del cart[str(jewelry_id)]
        request.session['cart'] = cart
    return redirect('cart_detail')

def watches_list(request):
    watches = Watch.objects.all()
    return render(request, 'shop/watches_list.html', {'watches': watches})

def add_pendant(request):
    if request.method == 'POST':
        form = PendantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pendants_list')
    else:
        form = PendantForm()
    return render(request, 'shop/add_pendant.html', {'form': form})

def edit_pendant(request, pendant_id):
    pendant = get_object_or_404(Pendant, id=pendant_id)
    if request.method == 'POST':
        form = PendantForm(request.POST, request.FILES, instance=pendant)
        if form.is_valid():
            form.save()
            return redirect('pendant_detail', pendant_id=pendant.id)
    else:
        form = PendantForm(instance=pendant)
    return render(request, 'shop/edit_pendant.html', {'form': form})

def delete_pendant(request, pendant_id):
    pendant = get_object_or_404(Pendant, id=pendant_id)
    pendant.delete()
    return redirect('pendants_list')

def jewelry_list(request):
    jewelries = Jewelry.objects.all()
    return render(request, 'shop/jewelry_list.html', {'jewelries': jewelries})

def rings_list(request):
    rings = Ring.objects.all()
    return render(request, 'shop/rings_list.html', {'rings': rings})

def earrings_list(request):
    earrings = Earring.objects.all()
    return render(request, 'shop/earrings_list.html', {'earrings': earrings})

def pendants_list(request):
    pendants = Pendant.objects.all()
    return render(request, 'shop/pendants_list.html', {'pendants': pendants})

def pendant_detail(request, pendant_id):
    pendant = get_object_or_404(Pendant, id=pendant_id)
    return render(request, 'shop/pendant_detail.html', {'pendant': pendant})

def bracelets_list(request):
    bracelets = Bracelet.objects.all()
    return render(request, 'shop/bracelets_list.html', {'bracelets': bracelets})

def watches_list(request):
    watches = Watch.objects.all()
    return render(request, 'shop/watches_list.html', {'watches': watches})

def charms_list(request):
    charms = Charm.objects.all()
    return render(request, 'shop/charms_list.html', {'charms': charms})

def jewelry_detail(request, type, id):
    jewelry = get_object_or_404(Jewelry, id=id)
    return render(request, 'shop/jewelry_detail.html', {'jewelry': jewelry})
