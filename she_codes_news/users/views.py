from django.urls import reverse_lazy
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm,CustomUserChangeForm
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User

User = CustomUser

# Create your views here.

class CreateAccountView(generic.edit.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'


class UserProfileView(generic.TemplateView):
    template_name = 'users/profile.html'


class EditAccountView(generic.edit.UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'users/editAccount.html'
    def get_success_url(self):
        return reverse_lazy('users:profile', kwargs={"username": self.request.user.username})
    slug_field = 'username'
    slug_url_kwarg = 'username'



