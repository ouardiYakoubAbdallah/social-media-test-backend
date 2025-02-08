from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse

from authentication_and_authorization.models import Follow

User = get_user_model()


class UserFollowTests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username='user1',
            email='user1@example.com',
            password='password123'
        )
        self.user2 = User.objects.create_user(
            username='user2',
            email='user2@example.com',
            password='password123'
        )
        self.client.login(email='user1@example.com', password='password123')

    def test_follow_user_success(self):
        url = reverse('follow', kwargs={'username': self.user2.username})
        response = self.client.post(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        is_following = Follow.objects.filter(user=self.user1, followed_user=self.user2).exists()
        self.assertTrue(is_following)

    def test_follow_user_failure_already_following(self):
        url = reverse('follow', kwargs={'username': self.user2.username})
        self.client.post(url, format='json')
        response = self.client.post(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
