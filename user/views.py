# user/views.py

# Import necessary classes and functions from Django for handling user authentication
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from .forms import ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required

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

# Register view for new users to create an account
def register(request):
  """
  Handles user registration. If the user is already logged in, redirect to the home page.
  If the request method is POST, it processes the registration form.
  """
  
  # If the user is authenticated, redirect to home page
  if request.user.is_authenticated:
    # Redirect to home page if the user is already logged in
    return redirect('home') 
  
  # If the request method is POST, process the registration form
  if request.method == 'POST':
    # Instantiate the registration form with the submitted data
    form = UserRegisterForm(request.POST)  
    # Check if the form is valid
    if form.is_valid():
      form.save()  # Save the form and create the user
      messages.success(request, 'Account created successfully! You can now log in.')
      # Redirect to login page after successful registration
      return redirect('login')  
  else:
    # If it's a GET request, create an empty form instance
    form = UserRegisterForm()  
  
  # Render the registration page with the form
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
def profile(request):
  """
  Renders the profile page for logged-in users.
  """
  return render(request, 'users/profile.html')

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
    p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
    
    # If both forms are valid, save the data
    if u_form.is_valid() and p_form.is_valid():
      u_form.save()  # Save the user form
      p_form.save()  # Save the profile form
      messages.success(request, 'Your profile has been updated successfully!')
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
