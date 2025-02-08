from django.urls import path
from .views import *

urlpatterns = [
    path('users', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('profile/<pk>', UserProfileView.as_view(), name='profile'),
    path('users/follow/<str:username>', FollowView.as_view(), name='follow')
]