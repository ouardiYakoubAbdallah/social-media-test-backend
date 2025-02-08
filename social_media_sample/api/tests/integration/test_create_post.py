from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class PostCreationTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='password123'
        )
        self.client.login(email='testuser@example.com', password='password123')

    def test_create_post_success(self):
        data = {
            'content': 'Hello world! This is a test post.',
        }
        url = reverse('posts')
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['content'], 'Hello world! This is a test post.')
        self.assertEqual(response.data['author']['id'], self.user.id)

    def test_create_post_unauthenticated(self):
        self.client.logout()
        data = {
            'content': 'Hello world! This is a test post.',
        }
        url = reverse('posts')
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
