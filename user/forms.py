# user/forms.py

# Import necessary Django modules for form creation
from django import forms  # Import forms module to define form fields
from django.contrib.auth.models import User  # Import User model to handle user-related forms
from django.contrib.auth.forms import UserCreationForm  # Import UserCreationForm for creating new users
from django.db import models  # Import models to define database fields in forms
from .models import Profile  # Import Profile model to handle profile-related forms

# User registration form that inherits from Django's UserCreationForm
class UserRegisterForm(UserCreationForm):
  # Define additional fields for user registration
  first_name = models.TextField(max_length=200)  
  last_name = models.TextField(max_length=200)  
  email = models.EmailField()  

  class Meta:
    # Use the built-in User model for form handling
    model = User  
    # Fields to display in the form
    fields = ['username', 'first_name', 'last_name', 'email']  

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
