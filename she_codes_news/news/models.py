from django.contrib.auth import get_user_model
from django.db import models


class NewsStory(models.Model):
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
    cuisine_type = models.CharField(
        max_length=30,
        choices=Cuisine_CHOICES,
        default='Other',
    )
    
    CHOICES = [('1','Awful'),('2','Average'),('3','Okay'),('4','Good'),('5','Fantastic')]
    Food_rating = models.CharField(
        max_length=20,
        choices=Cuisine_CHOICES,
        default=3,
    )

    title = models.CharField(max_length=200)
    Restaurant = models.CharField(max_length=200)

    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="stories"
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    image_upload = models.URLField(default="",max_length=500)
