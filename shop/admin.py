from django.contrib import admin
from django.utils.html import format_html
from .models import Jewelry, Cart, CartItem, Group, Ring, Earring, Pendant, Bracelet, Watch, Charm

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1

@admin.register(Jewelry)
class JewelryAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'jewelry_type', 'custom_description')
    list_filter = ('price',) 
    search_fields = ('name', 'description')
    readonly_fields = ('get_created_at', 'get_updated_at') 
    @admin.display(description='Описание')
    def custom_description(self, obj):
        return obj.description[:50]

    def jewelry_type(self, obj):
        return obj.__class__.__name__

    def get_created_at(self, obj):
        return obj.created_at
    get_created_at.short_description = 'Дата создания'

    def get_updated_at(self, obj):
        return obj.updated_at
    get_updated_at.short_description = 'Последнее обновление'

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    date_hierarchy = 'created_at'
    inlines = [CartItemInline]

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'jewelry', 'quantity')
    list_filter = ('cart__user', 'jewelry')
    raw_id_fields = ('cart', 'jewelry')

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Group, GroupAdmin)

class JewelryBaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'group', 'custom_description')
    list_filter = ('group',)
    search_fields = ('name', 'description')
    readonly_fields = ('get_created_at', 'get_updated_at') 

    @admin.display(description='Описание')
    def custom_description(self, obj):
        return obj.description[:50]

    def get_created_at(self, obj):
        return obj.created_at
    get_created_at.short_description = 'Дата создания'

    def get_updated_at(self, obj):
        return obj.updated_at
    get_updated_at.short_description = 'Последнее обновление'


@admin.register(Ring)
class RingAdmin(JewelryBaseAdmin):
    pass

@admin.register(Earring)
class EarringAdmin(JewelryBaseAdmin):
    pass

@admin.register(Pendant)
class PendantAdmin(JewelryBaseAdmin):
    pass

@admin.register(Bracelet)
class BraceletAdmin(JewelryBaseAdmin):
    pass

@admin.register(Watch)
class WatchAdmin(JewelryBaseAdmin):
    pass

@admin.register(Charm)
class CharmAdmin(JewelryBaseAdmin):
    pass
