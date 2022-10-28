from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

CLASSES = (
    ('JUNIOR SECONDARY SCHOOL 1', 'Junior Secondary School 1'),
    ('JUNIOR SECONDARY SCHOOL 2', 'Junior Secondary School 2'),
    ('JUNIOR SECONDARY SCHOOL 3', 'Junior Secondary School 3'),
    ('SENIOR SECONDARY SCHOOL 1', 'Senior Secondary School 1'),
    ('SENIOR SECONDARY SCHOOL 2', 'Senior Secondary School 2'),
    ('SENIOR SECONDARY SCHOOL 3', 'Senior Secondary School 3'),
)

class CustomUser(AbstractUser):
    # pass
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(blank=False)
    teacher = models.BooleanField(blank=False, default=False)
    student = models.BooleanField(blank=False, default=False)
    school_attend = models.CharField(max_length=150, blank=True)
    student_class = models.CharField(max_length=150, blank=True)
    teacher_school_teach = models.CharField(max_length=150, blank=True)
    teacher_class_teach = models.CharField(max_length=150, blank=True)
    professional_qualification_file = models.FileField(upload_to='Prof_qual/', blank=True)
    professional_qualification_url = models.URLField(blank=False)

    def __str__(self) -> str:
        return f'{self.first_name} {self.username}'




