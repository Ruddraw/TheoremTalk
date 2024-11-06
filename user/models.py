from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
  #one user shoul dhave only 1 profile
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  #bio
  bio = models.CharField(max_length=1000, default="")
  #email
  email = models.EmailField(default="")
  #image
  image = models.ImageField(default="default.jpg", upload_to="profile_pic")

  def __str__(self):
    return f'{self.user.username} - Profile'
  
