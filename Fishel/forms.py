from .models import GenerateQuestions
from django import forms
from django.forms import PasswordInput, models


class GenerateQuestionsForm(models.ModelForm):
    class Meta:
        model = GenerateQuestions
        fields = '__all__'