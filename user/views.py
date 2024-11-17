# user/views.py
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from .forms import ProfileUpdateForm, UserUpdateForm

class CustomLoginView(LoginView):
  # Specify custom template
  template_name = 'users/login.html'  
  def dispatch(self, request, *args, **kwargs):
    if request.user.is_authenticated:
      return redirect('home')  # Redirect if already logged in
    return super().dispatch(request, *args, **kwargs)
  
def register(request):
  if request.user.is_authenticated:
    return redirect('home')  # Redirect if already logged in
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'Account created successfully! You can now log in.')
      return redirect('login')
  else:
    form = UserRegisterForm()
  return render(request, 'users/register.html', {'form': form})

#we could avoid writing a new logout view if we use a button in the html. because Django’s LogoutView expects a POST request by default for security reasons. This requirement helps prevent CSRF attacks, ensuring users aren’t logged out without intentional action.
def logout_view(request):
  logout(request)
  return redirect('home')  # Redirect to home or another page after logout


def profile(request):
  return render(request, 'users/profile.html')

def update_profile(request):
  if request.method == 'POST':
    u_form = UserUpdateForm(request.POST, instance=request.user)
    p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
    
    if u_form.is_valid() and p_form.is_valid():
      u_form.save()
      p_form.save()
      messages.success(request, 'Your profile has been updated successfully!')
      return redirect('profile')  # Redirect to profile page after update
  else:
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)

  context = {
    'u_form': u_form,
    'p_form': p_form,
  }
  return render(request, 'users/update_profile.html', context)