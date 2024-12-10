# user/urls.py

# Import necessary Django modules and views for routing
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  # Importing Django's built-in authentication views
from .views import CustomLoginView  # Import custom views for login, register, and logout

# Define the app name to set the namespace for reverse lookups


# URL patterns that define the routing for various user-related pages
urlpatterns = [
  path('', views.home, name="home"),
  path('register/', views.register, name='register'),
  path('login/', CustomLoginView.as_view(), name='login'),
  path('logout/', views.logout_view, name='logout'),
  path('profile/<str:username>/', views.profile, name='profile'),
  path('users/', views.list_users, name='list_users'),
]
