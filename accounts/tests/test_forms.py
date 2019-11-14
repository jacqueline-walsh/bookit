from django.test import TestCase
from accounts.forms import LoginForm, RegisterForm

# Create your tests here.
class TestBookItLoginForm(TestCase):

  def test_can_login_with_just_a_username(self):
    form = LoginForm({'username': 'samSmith'})
    self.assertFalse(form.is_valid())
  
  def test_can_login_with_just_a_password(self):
    form = LoginForm({'password': 'password'})
    self.assertFalse(form.is_valid()) 

class TestBookItRegisterForm(TestCase):

  def test_correct_message_for_missing_firstname(self):
    form = RegisterForm({'first_name': ''})
    self.assertFalse(form.is_valid()) 
    self.assertEqual(form.errors['first_name'], [u'This field is required.'])
  
  def test_correct_message_for_missing_lastname(self):
    form = RegisterForm({'last_name': ''})
    self.assertFalse(form.is_valid()) 
    self.assertEqual(form.errors['last_name'], [u'This field is required.'])

  def test_correct_message_for_missing_username(self):
    form = RegisterForm({'username': ''})
    self.assertFalse(form.is_valid()) 
    self.assertEqual(form.errors['username'], [u'This field is required.'])

  def test_correct_message_for_missing_email(self):
    form = RegisterForm({'email': ''})
    self.assertFalse(form.is_valid()) 
    self.assertEqual(form.errors['email'], [u'This field is required.'])

  def test_correct_message_for_missing_password(self):
    form = RegisterForm({'password': ''})
    self.assertFalse(form.is_valid()) 
    self.assertEqual(form.errors['password'], [u'This field is required.'])

  def test_correct_message_for_missing_password_confirm(self):
    form = RegisterForm({'password_confirm': ''})
    self.assertFalse(form.is_valid()) 
    self.assertEqual(form.errors['password_confirm'], [u'This field is required.'])
