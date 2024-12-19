from django.db import models
from django.contrib.auth.models import User

class Jewelry(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='jewelry_images')

    class Meta:
        verbose_name = 'Jewelry'
        verbose_name_plural = 'Jewelry'

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    jewelry = models.ForeignKey(Jewelry, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'CartItem'
        verbose_name_plural = 'CartItems'

class Group(models.Model):
    name = models.CharField(max_length=100)  # Поле для названия группы

    class Meta:
        verbose_name = 'Group'  # Человекочитаемое название для единственного объекта
        verbose_name_plural = 'Groups'  # Человекочитаемое название для множественного числа объектов

    def __str__(self):
        return self.name  # Опциональный метод, возвращающий строковое представление объекта модели

class Ring(Jewelry):
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, related_name='rings')

    class Meta:
        verbose_name = 'Ring'
        verbose_name_plural = 'Rings'

class Earring(Jewelry):
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, related_name='earrings')

    class Meta:
        verbose_name = 'Earring'
        verbose_name_plural = 'Earrings'

class Pendant(Jewelry):
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, related_name='pendants')

    class Meta:
        verbose_name = 'Pendant'
        verbose_name_plural = 'Pendants'

class Bracelet(Jewelry):
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, related_name='bracelets')

    class Meta:
        verbose_name = 'Bracelet'
        verbose_name_plural = 'Bracelets'

class Watch(Jewelry):
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, related_name='watches')

    class Meta:
        verbose_name = 'Watch'
        verbose_name_plural = 'Watches'

class Charm(Jewelry):
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, related_name='charms')

    class Meta:
        verbose_name = 'Charm'
        verbose_name_plural = 'Charms'
