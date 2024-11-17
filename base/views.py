from django.shortcuts import render
from django.views.generic import ListView
from .models import Question
# Create your views here.
def home(request):
  return render(request, 'home.html')

#CRUD function
class QuestionListView(ListView):
  model = Question
  template_name = 'template/base/question_list.html'  # Adjust the path if needed
  context_object_name = 'questions'