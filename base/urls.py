from django.urls import path
from . import views

app_name = 'base'  # Make sure the app_name is correct

urlpatterns = [
    path('', views.home, name="home"),  # Home page URL
    path('questions/', views.QuestionListView.as_view(), name="question_list"),  # The list of questions
    # Other URL patterns for question detail, create, etc.
]