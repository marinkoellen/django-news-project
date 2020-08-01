from django import forms
from django.forms import ModelForm
from .models import NewsStory

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'author','pub_date','image_upload','content']
        widgets = {
            'pub_date': forms.DateInput(
                format=('%m/%d/%Y'),
                attrs={
                    'class': 'form_control',
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            )
            ,
            "content": forms.Textarea(
                attrs={'placeholder': 'Please write a riveting for my news paper'
                },
            )

        }