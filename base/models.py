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
  date_created = models.DateTimeField(auto_now_add=True)

  # Automatically updates to the current time on save
  date_updated = models.DateTimeField(auto_now=True)  

  # Add upvotes and downvotes fields
  upvotes = models.IntegerField(default=0)
  downvotes = models.IntegerField(default=0)

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

  # Methods for upvoting and downvoting
  def upvote(self):
    self.upvotes += 1
    self.save()

  def downvote(self):
    self.downvotes += 1
    self.save()

  # Meta class to define additional properties like ordering
  class Meta:
    # Ordering the questions by 'date_created' in descending order (newest first)
    ordering = ['-date_created']

class Reply(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='replies')
  question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='replies')
  text = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  # Add upvotes and downvotes fields
  upvotes = models.IntegerField(default=0)
  downvotes = models.IntegerField(default=0)

  def __str__(self):
    return f"Reply by {self.user.username} on {self.question.title}"
  
  # Methods for upvoting and downvoting
  def upvote(self):
    self.upvotes += 1
    self.save()

  def downvote(self):
    self.downvotes += 1
    self.save()
