from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    Cuisine_CHOICES = [
        ('French', 'French'),
        ('Italian', 'Italian'),
        ('Modern Australian', 'Modern Australian'),
        ('Indonesian', 'Indonesian'),
        ('Chinese', 'Chinese'),
        ('Japanese', 'Japanese'),
        ('Thai', 'Thai'),
        ('American', 'American'),
        ('Middle Eastern', 'Middle Eastern'),
        ('Indian', 'Indian'),
        ('Moroccan', 'Moroccan'),
        ('Other', 'Other'),
    ]
    favourite_cuisine = models.CharField(
        max_length=20,
        choices=Cuisine_CHOICES,
        default='Other',
    )

