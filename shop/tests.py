from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Pendant
from .forms import PendantForm

class PendantTestCase(TestCase):
    
    def setUp(self):
        # Подготовка данных для тестов
        self.pendant = Pendant.objects.create(
            name='Тестовая подвеска',
            description='Описание тестовой подвески',
            price=100.00,
            image=SimpleUploadedFile('pendant_image.jpg', b'content', content_type='image/jpeg')
        )
    
    def test_pendant_detail_view(self):
        # Тестирование представления для деталей подвески
        
        url = reverse('pendant_detail', args=[self.pendant.id])
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.pendant.name)
        self.assertContains(response, self.pendant.description)
    
    def test_add_pendant_view(self):
        # Тестирование представления для добавления новой подвески
        
        url = reverse('add_pendant')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        
        data = {
            'name': 'Новая подвеска',
            'description': 'Описание новой подвески',
            'price': 150.00,
            'image': SimpleUploadedFile('new_pendant.jpg', b'content', content_type='image/jpeg')
        }
        response = self.client.post(url, data, format='multipart')
        
        self.assertEqual(response.status_code, 302)  # Перенаправление после успешного добавления
    
    def test_edit_pendant_view(self):
        # Тестирование представления для редактирования существующей подвески
        
        url = reverse('edit_pendant', args=[self.pendant.id])
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        
        data = {
            'name': 'Отредактированная подвеска',
            'description': 'Новое описание подвески',
            'price': 120.00,
            'image': SimpleUploadedFile('edited_pendant.jpg', b'content', content_type='image/jpeg')
        }
        response = self.client.post(url, data, format='multipart')
        
        self.assertEqual(response.status_code, 302)  # Перенаправление после успешного редактирования
    
    def test_delete_pendant_view(self):
        # Тестирование представления для удаления подвески
        
        url = reverse('delete_pendant', args=[self.pendant.id])
        response = self.client.post(url)
        
        self.assertEqual(response.status_code, 302)  # Перенаправление после успешного удаления

    def test_cart_detail_view(self):
        # Тестирование представления корзины покупок
        
        url = reverse('cart_detail')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/cart_detail.html')
        self.assertIn('cart', response.context)
