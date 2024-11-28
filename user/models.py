# user/models.py

# Import necessary modules for model creation and image handling
from django.db import models  
from django.contrib.auth.models import User  
from PIL import Image  

# Define the Profile model to extend the User model with additional user-specific data
class Profile(models.Model):
  # Define a one-to-one relationship between the Profile and User model
  # Each user has one profile, and the profile is deleted if the user is deleted
  user = models.OneToOneField(User, on_delete=models.CASCADE)  

  # Define the bio field to store a short description about the user
  bio = models.CharField(max_length=1000, default="")  

  # Define the email field to store the user's email address
  email = models.EmailField(default="")  

  # Define the image field to store the user's profile image
  # Default image is set, and uploads go to 'profile_pic' directory
  image = models.ImageField(default="profile_pic/default.jpg", upload_to="profile_pic")  

  # String representation of the profile, showing the username of the associated user
  def __str__(self):
    return f'{self.user.username} - Profile'

  # Override the save method to handle image resizing
  def save(self, *args, **kwargs):
    # Call the parent class's save method to first save the profile data
    super().save(*args, **kwargs)

    # Open the image using PIL to check its dimensions
    img = Image.open(self.image.path)

    # If the image is larger than 300x300, resize it to fit within those dimensions
    if img.height > 300 or img.width > 300:
      # Define the maximum output size as a tuple (300, 300)
      output_size = (300, 300)  
      # Resize the image while maintaining aspect ratio
      img.thumbnail(output_size)  
      # Save the resized image back to the same path
      img.save(self.image.path)  
