from django import forms
from django.forms import ModelForm, SplitDateTimeField, SplitDateTimeWidget
from .models import NewsStory

class StoryForm(ModelForm):
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
    
    image_upload = forms.URLField(required=False, help_text='If image path is left blank, a randomly generated image will appear in your article',
    widget=forms.TextInput(attrs={'class': "form_entry"}))
    
    CHOICES = [('1','Awful'),('2','Average'),('3','Okay'),('4','Good'),('5','Fantastic')]
    Food_rating=forms.CharField(label='Overall Experience Rating', widget=forms.RadioSelect(choices=CHOICES))

    pub_date = SplitDateTimeField(
		# use split date time field to allow the user to input both date and time
        widget=SplitDateTimeWidget(
			# we use the split date time widget to specify how the html gets built
            date_attrs={'type': 'date', 'class':'form_entry'},
			# type date tells django to use the HTML5 date input
            time_attrs={'type': 'time','class':'form_entry'},
			# type time tells django to use the HTML5 time input
        )
    )

    class Meta:
        model = NewsStory
        fields = ['title','Restaurant', 'pub_date','image_upload','content','cuisine_type']
        widgets = {
            "content": forms.Textarea(
                attrs={'placeholder': 'We cannot wait to hear where you have eaten and what it was like!','class':'form_entry' },
                )
                ,

            "title": forms.TextInput(
                attrs={
                'class':'form_entry'}
                )
                ,
            "Restaurant": forms.TextInput(
                attrs={
                'class':'form_entry'}
            )    
        }


class StoryFormChangeForm(ModelForm):
    image_upload = forms.URLField(required=False, help_text='If image path is left blank, a randomly generated image will appear in your article',
    widget=forms.TextInput(attrs={'class': "form_entry"}))
    CHOICES = [('1','Awful'),('2','Average'),('3','Okay'),('4','Good'),('5','Fantastic')]
    Food_rating=forms.CharField(label='Overall Experience Rating', widget=forms.RadioSelect(choices=CHOICES))
    pub_date = SplitDateTimeField(
            # use split date time field to allow the user to input both date and time
            widget=SplitDateTimeWidget(
                # we use the split date time widget to specify how the html gets built
                date_attrs={'type': 'date', 'class':'form_entry'},
                # type date tells django to use the HTML5 date input
                time_attrs={'type': 'time','class':'form_entry'},
                # type time tells django to use the HTML5 time input
            )
        )


    class Meta:
        model = NewsStory
        fields = ['title','Restaurant', 'pub_date','image_upload','content','cuisine_type']
        widgets = {
            "content": forms.Textarea(
                attrs={'placeholder': 'We cannot wait to hear where you have eaten and what it was like!','class':'form_entry' },
                )
                ,

            "title": forms.TextInput(
                attrs={
                'class':'form_entry'}
                )
                ,
            "Restaurant": forms.TextInput(
                attrs={
                'class':'form_entry'}
            )    
        }    
        


class UserDeleteForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = []   #Form has only submit button.  Empty "fields" list still necessary, though.