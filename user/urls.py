# user/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomLoginView, register, logout_view

urlpatterns = [
  path('register/', views.register, name='register'),
  path('login/', CustomLoginView.as_view(), name='login'),
  path('logout/', views.logout_view, name='logout'),  

]
 