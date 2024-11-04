from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class RegistrationViewTests(TestCase):
  """
    Tests for the Registration View.
    
    This class contains tests for the registration view to ensure that:
    - The GET request successfully renders the registration page.
    - The POST request creates a new user when valid data is provided.
  """
  def setUp(self):
    self.client = Client()
    self.register_url = reverse('register')
  
  def test_register_view_GET(self):
    response = self.client.get(self.register_url)
    self.assertEqual(response.status_code, 200)
    # Check that the correct template is used for the registration page
    self.assertTemplateUsed(response, 'users/register.html')
  
  def test_register_view_POST(self):
    response = self.client.post(self.register_url, {
      'username': 'testuser',
      'first_name': 'Test',
      'last_name': 'User',
      'email': 'test@example.com',
      'password1': 'TestPassword123!',
      'password2': 'TestPassword123!',
    })
    # Expect redirect after successful registration
    self.assertEqual(response.status_code, 302) 
    # Verify that the user was created in the database 
    self.assertTrue(User.objects.filter(username='testuser').exists())

class LoginViewTests(TestCase):
  """
    Tests for the Login View.
    
    This class contains tests for the login view to ensure that:
    - The GET request successfully renders the login page.
    - The POST request authenticates the user when valid credentials are provided.
  """
  def setUp(self):
    self.client = Client()
    self.login_url = reverse('login')
    # Create a test user for login
    self.user = User.objects.create_user(username='testuser', password='testpassword123')

  def test_login_view_GET(self):
    # Test that the login view returns a 200 status code on GET request
    response = self.client.get(self.login_url)
    self.assertEqual(response.status_code, 200)
    # Check that the correct template is used for the login page
    self.assertTemplateUsed(response, 'users/login.html')

  def test_login_view_POST(self):
    # Test the login view with valid credentials
    response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'testpassword123'})
    # Expect redirect after login
    self.assertEqual(response.status_code, 302)
    # Verify that the user is authenticated after login  
    self.assertTrue(response.wsgi_request.user.is_authenticated)

class LogoutViewTests(TestCase):
  """
    Tests for the Logout View.
    
    This class contains tests for the logout view to ensure that:
    - The user is successfully logged out and redirected.
    - The user is no longer authenticated after logging out.
  """
  def setUp(self):
    #create test client
    self.client = Client()
    #create test user and log in
    self.user = User.objects.create_user(username='testuser', password='testpassword123')
    self.client.login(username='testuser', password='testpassword123')
  
  def test_logout_view(self):
    response = self.client.get(reverse('logout'))
    # Redirect after logout
    self.assertEqual(response.status_code, 302)  
    # Verify that the user is no longer authenticated after logout
    response = self.client.get(reverse('logout'))
    self.assertFalse(response.wsgi_request.user.is_authenticated)
