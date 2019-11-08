# from django.test import TestCase
# from django.contrib.auth.models import User
# from django.urls import reverse
# from django.test.client import Client


# # Create your tests here.
# class TestAccountsViews(TestCase):

#   def test_get_register_page(self):
#     response = self.client.get('/accounts/register')
#     self.assertEqual(response.status_code, 200)
#     self.assertTemplateUsed(response, 'accounts/register.html')

#   def test_get_login_page(self):
#     response = self.client.get('/accounts/login/')
#     self.assertEqual(response.status_code, 200)
#     self.assertTemplateUsed(response, 'accounts/login.html')

#   def setUp(self):
#     self.client = Client()
#     self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

#   def testLogin_get_profile_page(self):
#     self.client.login(username='john', password='johnpassword')
#     response = self.client.get(reverse('index.html'))
#     response = self.client.get('/accounts/profile/')
#     self.assertEqual(response.status_code, 200)
#     self.assertTemplateUsed(response, 'accounts/profile.html')        
#     self.assertEqual(response.status_code, 200)

