from rest_framework import serializers
from .models import *


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

    def get_author(self, obj):
        return {
            "id": obj.author.id,
            "username": obj.author.username,
            "email": obj.author.email
        }
