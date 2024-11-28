# user/signals.py

# Import necessary modules for Django signals
from django.db.models.signals import post_save  # Import post_save signal that triggers after saving an object
from django.contrib.auth.models import User  # Import the User model from Django's authentication system
from django.dispatch import receiver  # Import the receiver decorator to handle signals
from .models import Profile  # Import the Profile model from the current app

# Receiver function that creates a Profile when a new User is created
@receiver(post_save, sender=User)  # This decorator connects the signal to the function
def create_profile(sender, instance, created, **kwargs):
  """
  This function is triggered when a new User object is created.
  It automatically creates a corresponding Profile for the new user.
  """
  if created:
    # Create a new profile instance for the newly created user
    Profile.objects.create(user=instance)

# Receiver function that saves the Profile whenever the User object is saved
@receiver(post_save, sender=User)  # This decorator connects the signal to the function
def save_profile(sender, instance, **kwargs):
  """
  This function is triggered when the User object is saved.
  It ensures that the associated Profile is also saved.
  """
  instance.profile.save()  # Save the related profile after saving the user
