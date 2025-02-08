from django.test import TestCase
from django.contrib.auth import get_user_model

from api.serializers import PostSerializer
from api.models import Post

User = get_user_model()


class PostSerializerTest(TestCase):
    def test_post_serializer(self):
        user = User(username="author", email="author@sample.io")
        post = Post(content="Test post", author=user)
        serializer = PostSerializer(post)

        self.assertEqual(serializer.data["content"], "Test post")
        self.assertEqual(serializer.data["author"]["username"], "author")