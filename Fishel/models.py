from django.db import models

# Create your models here.

SUBJECT = (
    ('MATH', 'Mathematics'),
    ('ENGLISH', 'English Language'),
)

# class GenerateQuestions(models.Model):
#     subject = models.CharField(choices=SUBJECT, max_length=30, default=1)
#     topics 


class MathematicsFoundation(models.Model):
    topics = models.CharField(max_length=150)


class MathematicsHigher(models.Model):
    topics = models.CharField(max_length=150)


class MathematicsFoundation_Images(models.Model):
    images = models.ImageField(upload_to='mathematics_foundation/')
    topics = models.ForeignKey(MathematicsFoundation, on_delete=models.CASCADE)


class MathematicsHigher_Images(models.Model):
    images = models.ImageField(upload_to='mathematics_higher/')
    topics = models.ForeignKey(MathematicsHigher, on_delete=models.CASCADE)

