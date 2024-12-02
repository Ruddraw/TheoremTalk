# base/views.py

# Import necessary modules from Django
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from .models import Question


# Home view function to render the homepage


def home(request):
    """
    Renders the 'home.html' template for the homepage.
    """
    # Rendering the 'home.html' template when the home view is accessed
    return render(request, 'home.html')


# CRUD (Create, Read, Update, Delete) Views for the 'Question' model

# List view to display all questions
class QuestionListView(ListView):
    """
    List view for displaying a list of all questions.
    Uses the 'Question' model and the 'question_list.html' template.
    """
    # Specifying the model to be used (Question)
    model = Question

    # Defining the template for rendering the list of questions
    template_name = 'template/base/question_list.html'

    # The context variable to be used in the template
    context_object_name = 'questions'


# Detail view to display a single question's details
class QuestionDetailView(DetailView):
    """
    Detail view for displaying a single question's details.
    Uses the 'Question' model.
    """
    # Specifying the model to be used (Question)
    model = Question
    
    # The context variable to be used in the template
    context_object_name = 'question'
    
    # The template for displaying the question details
    template_name = 'base/question_detail.html'


# Create view for adding a new question
class QuestionCreateView(CreateView):
    """
    Create view for adding a new question. 
    Requires a 'title' and 'content' to create a question.
    """
    # Specifying the model to be used (Question)
    model = Question

    # Fields to be displayed in the form for creating a question
    fields = ['title', 'content']

    # Use your existing 'question_form.html' template
    template_name = 'base/question_form.html'

    def form_valid(self, form):
        """
        Custom logic for handling a valid form submission. 
        The user is automatically set to the current logged-in user.
        """
        # Assigning the current user to the question instance
        form.instance.user = self.request.user

        # Debugging: Print form data to the console for verification
        print("Title:", form.cleaned_data['title'])
        print("Content:", form.cleaned_data['content'])

        # Proceeding with the default form submission behavior
        return super().form_valid(form)
    
    
