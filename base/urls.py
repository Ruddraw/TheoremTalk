from django.urls import path
from . import views

app_name = 'base'  

urlpatterns = [
  path('', views.home, name="home"),  # Home page URL
  path('questions/', views.QuestionListView.as_view(), name="question_list"), # The list of questions
  path('questions/<int:pk>', views.QuestionDetailView.as_view(), name="question_detail"),
]