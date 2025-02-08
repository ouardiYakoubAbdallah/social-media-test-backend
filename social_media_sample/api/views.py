from rest_framework import generics, status, permissions
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer


class PostsFeedView(generics.GenericAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    allowed_methods = ['GET', 'POST']

    def get_queryset(self):
        followed_users = self.request.user.following.values_list('followed_user', flat=True)
        return Post.objects.filter(author__in=followed_users).order_by('-timestamp')

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
