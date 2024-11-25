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

    def form_valid(self, form):
        form.instance.user = self.request.user  # Set the user
        # Debugging: Print form data
        print("Title:", form.cleaned_data['title'])
        print("Content:", form.cleaned_data['content'])
        return super().form_valid(form)
