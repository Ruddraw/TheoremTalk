# user/forms.py

# Import necessary Django modules for form creation
from django import forms 
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from django.db import models 
from .models import Profile 

# User registration form that inherits from Django's UserCreationForm
class UserRegisterForm(UserCreationForm):
  first_name = forms.CharField(max_length=200, required=True)
  last_name = forms.CharField(max_length=200, required=True)
  email = forms.EmailField(required=True)

  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

  def save(self, commit=True):
    user = super().save(commit=False)
    if commit:
      user.set_password(self.cleaned_data['password1'])
      user.save()
    return user

# User update form for updating existing user information
class UserUpdateForm(forms.ModelForm):
  # Email field for updating the email
  email = forms.EmailField()

  class Meta:
    model = User  
    # Fields to display in the form
    fields = ['username', 'first_name', 'last_name', 'email']  

# Profile update form for updating user profile-related information
class ProfileUpdateForm(forms.ModelForm):
  class Meta:
    model = Profile  
    # Specify fields to include in the profile update form
    fields = ['bio', 'image']  
