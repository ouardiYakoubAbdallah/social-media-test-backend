from django.urls import path
from .views import *


urlpatterns = [
    path('', PostsFeedView.as_view(), name='posts')
]