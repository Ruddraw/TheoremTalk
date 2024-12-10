# base/views.py

# Import necessary modules from Django
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Question
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from .forms import ReplyForm
from django.db.models import Count
from django.views.generic.edit import DeleteView




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

    def get_queryset(self):
        """
        Override to annotate each question with the count of related replies.
        """
        return Question.objects.annotate(num_replies=Count('replies')).all()
    

# Detail view to display a single question's details
class QuestionDetailView(DetailView):
    """
    Detail view for displaying a single question's details.
    Allows users to submit replies.
    """
    model = Question
    context_object_name = 'question'
    template_name = 'base/question_detail.html'

    def get_context_data(self, **kwargs):
        """
        Override to include the reply form in the context.
        """
        context = super().get_context_data(**kwargs)
        
        # Add the reply form to the context
        context['reply_form'] = ReplyForm()

        # Add all replies related to this question to the context
        context['replies'] = self.object.replies.all()

        return context

    def post(self, request, *args, **kwargs):
        """
        Handle the form submission for replies.
        """
        question = self.get_object()  # Get the question object
        if request.user.is_authenticated:
            # Handle the reply form submission
            reply_form = ReplyForm(request.POST)
            if reply_form.is_valid():
                # Create the reply and associate it with the user and question
                reply = reply_form.save(commit=False)
                reply.user = request.user
                reply.question = question
                reply.save()
                return redirect('base:question_detail', pk=question.pk)
        else:
            # If the user is not authenticated, you can either return an error or redirect
            return redirect('user:login')  # Or handle as per your requirements


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

# Create view for updating a question
class QuestionUpdateView(UpdateView):
    """
    Update view for editing an existing question.
    """
    model = Question
    fields = ['title', 'content']
    template_name = 'base/question_form.html'

    def get_object(self):
        """
        Ensure that the user can only update their own question.
        """
        question = get_object_or_404(Question, pk=self.kwargs['pk'])
        if question.user != self.request.user:
            # If the user is not the owner, redirect or raise an error
            raise PermissionDenied(
                "You are not allowed to edit this question.")
        return question

    def form_valid(self, form):
        """
        Custom logic for handling a valid form submission.
        The user is automatically set to the current logged-in user.
        """
        form.instance.user = self.request.user
        return super().form_valid(form)

class QuestionDeleteView(DeleteView):
    """
    View to delete a question.
    Ensures that only the question's author can delete it.
    """
    model = Question
    template_name = 'base/question_confirm_delete.html'
    success_url = reverse_lazy('base:question_list')

    def get_object(self, queryset=None):
        question = super().get_object(queryset)
        if question.user != self.request.user:
            raise PermissionDenied("You are not allowed to delete this question.")
        return question