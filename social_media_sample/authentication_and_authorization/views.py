from rest_framework import generics, status, permissions
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as LoginSerializer

from .serializers import RegisterSerializer, UserSerializer
from .models import Follow

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer


class LoginView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer
    allowed_methods = ['POST']

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class UserProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    lookup_field = 'pk'


class FollowView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    allowed_methods = ['POST']

    def post(self, request, *args, **kwargs):
        username = kwargs.get('username')
        try:
            target_user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(
                {'detail': 'User not found.'},
                status=status.HTTP_404_NOT_FOUND
            )

        current_user = request.user
        if current_user == target_user:
            return Response(
                {'detail': 'You cannot follow yourself.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if Follow.objects.filter(user=current_user, followed_user=target_user).exists():
            return Response(
                {'detail': f'You are already following {target_user.username}'},
                status=status.HTTP_400_BAD_REQUEST
            )

        Follow.objects.create(user=current_user, followed_user=target_user)
        return Response({'message': f'You are now following {target_user.username}'}, status=status.HTTP_201_CREATED)
