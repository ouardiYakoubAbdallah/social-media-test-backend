from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse


class UserRegistrationTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_register_user_success(self):
        url = reverse('register')
        data = {'email': 'test@sample.io', 'username': 'testuser', 'password': 'testpass'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('username', response.data)

    def test_register_user_failure(self):
        url = reverse('register')
        data = {'email': 'test@sample.io', 'username': '', 'password': 'testpass'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 400)
