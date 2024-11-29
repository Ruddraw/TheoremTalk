# user/urls.py

# Import necessary Django modules and views for routing
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  # Importing Django's built-in authentication views
from .views import CustomLoginView, register, logout_view  # Import custom views for login, register, and logout

# URL patterns that define the routing for various user-related pages
urlpatterns = [
  # Home page URL that renders the home view
  path('', views.home, name="home"),
  
  # Register URL that renders the registration page and processes registration requests
  path('register/', views.register, name='register'),
  
  # Login URL that uses the custom login view defined in views.py
  path('login/', CustomLoginView.as_view(), name='login'),
  
  # Logout URL that triggers the logout view and logs out the user
  path('logout/', views.logout_view, name='logout'),

  path('profile/<str:username>/', views.profile, name='profile'),
]
