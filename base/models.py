# base/models.py

# Import necessary modules for model creation
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# Model for representing a question in the database
class Question(models.Model):
  """
  This model represents a Question created by a user. It contains fields like the 
  user who created the question, the title, content, and the date of creation.
  """
  
  # Foreign key relationship to the User model, representing the user who created the question
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  # Field to store the title of the question, with a maximum length of 1000 characters
  title = models.CharField(max_length=1000)
  
  # Field to store the content of the question, which can be blank or null
  content = models.TextField(null=True, blank=True)
  
  # DateTime field to store the creation date of the question, defaults to the current time
  date_created = models.DateTimeField(default=timezone.now)

  # String representation of the question, used for displaying the question in the admin interface
  def __str__(self):
    return f'{self.user.username} - Question'

  # Method to get the absolute URL for a question, used for redirection after a successful form submission
  def get_absolute_url(self):
    """
    Returns the URL to view the details of the question.
    Uses the primary key of the question to generate the URL.
    """
    return reverse('base:question_detail', kwargs={'pk': self.pk})

  # Meta class to define additional properties like ordering
  class Meta:
    # Ordering the questions by 'date_created' in descending order (newest first)
    ordering = ['-date_created']
