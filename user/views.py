# user/views.py

# Import necessary classes and functions from Django for handling user authentication
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from base.models import Question, Reply
from django.contrib.auth.models import User

# Custom LoginView to handle login with a custom template and prevent logged-in users from accessing the login page


class CustomLoginView(LoginView):
    """
    Custom login view to specify the template used for the login page.
    If the user is already authenticated, they will be redirected to the home page.
    """

    # Specify the template to be used for the login page
    template_name = 'users/login.html'

    def dispatch(self, request, *args, **kwargs):
        """
        Override the dispatch method to check if the user is authenticated.
        If authenticated, redirect to the home page.
        """

        # If the user is already logged in, redirect to home
        if request.user.is_authenticated:
            # Redirect to home page if the user is already logged in
            return redirect('home')

        return super().dispatch(request, *args, **kwargs)

# Home view function to render the homepage


def home(request):
    """
    Renders the home page.
    """
    return render(request, 'home.html')


def register(request):
    """
    Handles user registration. If the user is already logged in, redirect to the home page.
    If the request method is POST, it processes the registration form.
    """
    if request.user.is_authenticated:
        return redirect('home')  # Redirect if already logged in

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            messages.success(
                request, 'Your account has been created! You can now log in.')
            # Use the user namespace for the login view
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})

# Logout view to log the user out and redirect them to the homepage
# We could use a logout button in HTML since Django’s LogoutView requires a POST request for security reasons.


def logout_view(request):
    """
    Logs out the user and redirects them to the home page.
    """

    # Logout the user
    logout(request)
    # Redirect to home page after logging out
    return redirect('home')

# Profile view that requires the user to be logged in to access


@login_required
def profile(request, username):
    """
    Renders the profile page for the specified user.
    """
    # Get the user by the username or return a 404 error
    profile_user = get_object_or_404(User, username=username)

    # Fetch all questions posted by the user
    user_questions = Question.objects.filter(user=profile_user)

    # Fetch all questions the user has replied to
    replied_questions = Reply.objects.filter(
        user=profile_user).values('question').distinct()
    replied_question_ids = [reply['question'] for reply in replied_questions]
    replied_questions = Question.objects.filter(id__in=replied_question_ids)

    # Pass the data to the template
    return render(request, 'users/profile.html', {
        'profile_user': profile_user,
        'questions': user_questions,
        'replied_questions': replied_questions,
    })


# Update profile view to allow logged-in users to update their profile information
@login_required
def update_profile(request):
    """
    Allows logged-in users to update their profile and personal information.
    If the form is valid, the changes are saved and the user is redirected to their profile page.
    """

    # If the request method is POST, process the submitted data
    if request.method == 'POST':
        # Instantiate user and profile update forms with the submitted data
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)

        # If both forms are valid, save the data
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()  # Save the user form
            p_form.save()  # Save the profile form
            messages.success(
                request, 'Your profile has been updated successfully!')
            # Redirect to profile page after successful update
            return redirect('profile')
    else:
        # If it's a GET request, pre-populate the forms with the current user and profile data
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    # Prepare context to pass to the template for rendering
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    # Render the update profile page with the context data
    return render(request, 'users/update_profile.html', context)

# lists all the under of the webpage


def list_users(request):
    """
    View to display all active users who have not been deleted.
    Users are displayed as clickable cards/buttons with their profile pictures.
    Clicking on a user's name takes you to their profile page.
    """
    # Filter only active users (exclude deleted users)
    # Django sets `is_active` to False for deleted users.
    active_users = User.objects.filter(is_active=True)

    # Pass active users to the template
    return render(request, 'users/list_users.html', {'users': active_users})
