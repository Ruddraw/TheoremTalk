# base/admin.py

# Import necessary modules 
from django.contrib import admin
from .models import Question

# Register the Question model with the Django admin site
# This will allow to manage Question objects through the Django admin interface
admin.site.register(Question)