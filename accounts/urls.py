from django.urls import path, include
from . import views as auth_views

urlpatterns = [
    path('register/', auth_views.user_create_view, name='register'),
    path('login/', auth_views.user_login_view, name='login_page'),
    # path('', include('djoser.urls')),
]