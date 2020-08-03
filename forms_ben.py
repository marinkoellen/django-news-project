from django import forms
from django.forms import ModelForm, SplitDateTimeField, SplitDateTimeWidget

from .models import NewsStory


class StoryForm(ModelForm):
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
