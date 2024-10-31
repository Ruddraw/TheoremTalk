# user/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
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