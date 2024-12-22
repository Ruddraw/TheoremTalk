# base/urls.py

# Import necessary modules from Django
from django.urls import path
from . import views

# Namespace for the app, used to distinguish URLs within this app
app_name = 'base'

# Defining URL patterns for this app
urlpatterns = [
  # URL for the home page, mapped to the home view
  path('', views.home, name="home"),  
  
  # URL for displaying the list of questions, mapped to the QuestionListView
  path('questions/', views.QuestionListView.as_view(), name="question_list"), 
  
  # URL for creating a new question, mapped to the QuestionCreateView
  path('questions/new', views.QuestionCreateView.as_view(), name="question_create"),
  
  # URL for viewing details of a single question, mapped to the QuestionDetailView
  # The <int:pk> part captures the primary key of the question and passes it to the view
  path('questions/<int:pk>', views.QuestionDetailView.as_view(), name="question_detail"),

  # updating a question
  path('questions/<int:pk>/edit', views.QuestionUpdateView.as_view(), name="question_update"),

  # deleting the quesiton
  path('questions/<int:pk>/delete/', views.QuestionDeleteView.as_view(), name='question_delete'),

  #voting urls
  path('upvote_question/<int:question_id>/', views.upvote_question, name='upvote_question'),
  path('downvote_question/<int:question_id>/', views.downvote_question, name='downvote_question'),
  path('upvote_reply/<int:reply_id>/', views.upvote_reply, name='upvote_reply'),
  path('downvote_reply/<int:reply_id>/', views.downvote_reply, name='downvote_reply'),

 

]
