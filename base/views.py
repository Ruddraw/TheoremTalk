from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Question
# Create your views here.
def home(request):
  return render(request, 'home.html')

#CRUD function
class QuestionListView(ListView):
  model = Question
  template_name = 'template/base/question_list.html'  
  context_object_name = 'questions'

class QuestionDetailView(DetailView):
  model = Question
  
class QuestionCreateView(CreateView):
  model = Question
  fields = ['title', 'content']