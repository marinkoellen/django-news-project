from django import forms
from django.forms import ModelForm, SplitDateTimeField, SplitDateTimeWidget
from .models import NewsStory

class StoryForm(ModelForm):
    image_upload = forms.URLField(required=False, help_text='If image path is left blank, a randomly generated image will appear in your article')

    pub_date = SplitDateTimeField(
		# use split date time field to allow the user to input both date and time
        widget=SplitDateTimeWidget(
			# we use the split date time widget to specify how the html gets built
            date_attrs={'type': 'date'},
			# type date tells django to use the HTML5 date input
            time_attrs={'type': 'time'},
			# type time tells django to use the HTML5 time input
        )
    )

    class Meta:
        model = NewsStory
        fields = ['title', 'author','pub_date','image_upload','content']
        widgets = {
            # 'pub_date': forms.DateInput(
            #     format=('%m/%d/%Y'),
            #     attrs={
            #         'class': 'form_control',
            #         'placeholder': 'Select a date',
            #         'type': 'date'
            #     }
            # )
            # ,
            "content": forms.Textarea(
                attrs={'placeholder': 'Please write a riveting for my news paper'
                },
            )
            # ,

            # "image_upload": forms.URLField(
            #     attrs={ 'help_text': 'If image path is left blank, a randomly generated image will appear in your article' }
            # )
        

        }