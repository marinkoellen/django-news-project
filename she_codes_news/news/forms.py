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
        fields = ['title','pub_date','image_upload','content']
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


# Model metadata is “anything that’s not a field”, such as ordering options (ordering), database table name (db_table), or human-readable singular and plural names (verbose_name and verbose_name_plural). None are required, and adding class Meta to a model is completely optional. 

# A metaclass is the class of a class. A class defines how an instance of the class (i.e. an object) behaves while a metaclass defines how a class behaves. A class is an instance of a metaclass.

# metaclasses therefore allow you to do 'extra things' when creating a class, like registering the new class with some registry or replace the class with something else entirely.

#Meta inner class in Django models:

# This is just a class container with some options (metadata) attached to the model. It defines such things as available permissions, associated database table name, whether the model is abstract or not, singular and plural versions of the name etc.


#time_attrs={'type': 'time' PUT DEFAULTS AND CLASSES IN HERE EVERYTHING IN HERE},