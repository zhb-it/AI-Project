# users/tests/test_registration.py
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from .models import User


class UserRegistrationTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_register_user(self):
        url = reverse('users:register')

        data = {
            'email': 'test@example.com',
            'phone': '+1234567890',
            'date_of_birth': '1990-01-01',
            'password': 'securepassword123'
        }
        response = self.client.post(url, data, format='multipart')
        print(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['email'], 'test@example.com')
        self.assertTrue(User.objects.filter(email='test@example.com').exists())
