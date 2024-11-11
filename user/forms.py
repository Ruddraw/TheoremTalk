from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from .models import profile
class UserRegisterForm(UserCreationForm):
  first_name = models.TextField(max_length=200)
  last_name = models.TextField(max_length=200)
  email = models.EmailField()

  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']

class UserUpdateForm(forms.ModelForm):
  email = forms.EmailField()

  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']

class ProfileUpdateForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['username', 'first_name', 'last_name', 'email', 'bio', 'image']