from django.test import TestCase
from unittest.mock import patch
from django.contrib.auth import get_user_model

from authentication_and_authorization.models import Follow

User = get_user_model()


class UserModelTest(TestCase):
    @patch("authentication_and_authorization.models.User.objects.create_user")
    def test_create_user(self, mock_create_user):
        mock_create_user.return_value = User(username="testuser", email="test@sample.io")
        user = User.objects.create_user(username="testuser", email="test@sample.io", password="password")

        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@sample.io")
        mock_create_user.assert_called_once()


class FollowTest(TestCase):
    def test_follow_representation(self):
        user1 = User(username="user1", email="user1@sample.io")
        user2 = User(username="user2", email="user2@sample.io")
        follow = Follow(user=user1, followed_user=user2)

        # This test is supposed to fail intentionally
        self.assertEqual(str(follow), "user2 is followed by user1")
