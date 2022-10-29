from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home_page'),
    path('generate/', views.generate_question_view, name='generate_questions'),
    path('test/', views.generating_questions, name='test'),

]

