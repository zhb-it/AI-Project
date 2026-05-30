# users/tests/test_registration.py
# from django.test import TestCase
# from django.urls import reverse
# from rest_framework.test import APIClient
#
# from .models import User
#
#
# class UserRegistrationTest(TestCase):
#     """ 注册功能测试 """
#     def setUp(self):
#         self.client = APIClient()
#
#     def test_register_user(self):
#         url = reverse('users:register')
#
#         data = {
#             'email': 'test@example.com',
#             'phone': '+1234567890',
#             'date_of_birth': '1990-01-01',
#             'password': 'securepassword123'
#         }
#         response = self.client.post(url, data, format='multipart')
#         print(response.data)
#         self.assertEqual(response.status_code, 201)
#         self.assertEqual(response.data['email'], 'test@example.com')
#         self.assertTrue(User.objects.filter(email='test@example.com').exists())


# users/tests/test_login.py
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

class UserLoginTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email='test@example.com',
            password='securepassword123'
        )

    def test_login_success(self):
        url = reverse('users:login')
        data = {'email': 'test@example.com', 'password': 'securepassword123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)