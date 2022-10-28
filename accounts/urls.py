from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.user_create_view, name='register'),
    path('', include('djoser.urls')),
]