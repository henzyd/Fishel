from django.db import models

# Create your models here.

SUBJECT = (
    ('MATH', 'Mathematics'),
    ('ENGLISH', 'English Language'),
)

DIFFICULTY_LEVEL = (
    ('FOUNDATION', 'Foundation'),
    ('HIGHER', 'Higher'),
)


# class GenerateQuestions(models.Model):
#     subject = models.CharField(choices=SUBJECT, max_length=30, default=1)
#     topics 


# class Physics(models.Model):
    # name = models.CharField(defualt='Physics', max_lenght=100)


class PhysicsFoundation(models.Model):
    topics = models.CharField(max_length=150)
    def __str__(self) -> str:
        return f'{self.topics}'


class PhysicsHigher(models.Model):
    topics = models.CharField(max_length=150)

    def __str__(self) -> str:
        return f'{self.topics}'


class PhysicsFoundation_Images(models.Model): ## NOTE: Name this Foundation_Images
    images = models.ImageField(upload_to='mathematics_foundation/')
    topics = models.ForeignKey(PhysicsFoundation, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.images} --- {self.topics}'


class PhysicsHigher_Images(models.Model):
    images = models.ImageField(upload_to='mathematics_higher/')
    topics = models.ForeignKey(PhysicsHigher, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.images} --- {self.topics}'



class GenerateQuestions(models.Model):
    subject = models.CharField(choices=SUBJECT, max_length=30)
    difficulty_level = models.CharField(choices=DIFFICULTY_LEVEL, max_length=30)
