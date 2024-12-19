from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart_detail, name='cart_detail'),
    path('add_to_cart/<int:jewelry_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('remove_from_session_cart/<int:jewelry_id>/', views.remove_from_session_cart, name='remove_from_session_cart'),
    path('pendant/add/', views.add_pendant, name='add_pendant'),
    path('pendant/edit/<int:pendant_id>/', views.edit_pendant, name='edit_pendant'),
    path('pendant/delete/<int:pendant_id>/', views.delete_pendant, name='delete_pendant'),
    path('watches/', views.watches_list, name='watches_list'),
    path('pendants/', views.pendants_list, name='pendants_list'),
    path('pendant/<int:pendant_id>/', views.pendant_detail, name='pendant_detail'),
    path('rings/', views.rings_list, name='rings_list'),
    path('earrings/', views.earrings_list, name='earrings_list'),
    path('bracelets/', views.bracelets_list, name='bracelets_list'),
    path('charms/', views.charms_list, name='charms_list'),
    path('jewelry/<str:type>/<int:id>/', views.jewelry_detail, name='jewelry_detail'),
    path('', views.jewelry_list, name='jewelry_list'),
]
