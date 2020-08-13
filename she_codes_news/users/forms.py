from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,ReadOnlyPasswordHashField
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username','email','bio','location','favourite_cuisine','password']
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user



class CustomUserChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField(label="",
        help_text=("")
    )

    class Meta:
        model = CustomUser
        fields = ['username','email','bio','location','favourite_cuisine','password']



  