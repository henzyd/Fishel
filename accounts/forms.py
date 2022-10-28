from django import forms
from django.contrib.auth.models import User
from django.forms import PasswordInput, models
from django.contrib.auth import get_user_model
from .models import CustomUser


User = get_user_model()


class UserRegistrationForm(models.ModelForm, forms.Form):

    # password = forms.CharField(widget=forms.PasswordInput())
    # password_2 = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password', 'teacher', 'student', 'school_attend', 'student_class', 'teacher_school_teach', 'teacher_class_teach', 'professional_qualification_file', 'professional_qualification_url']

