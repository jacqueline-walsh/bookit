from django.test import TestCase
from django.contrib.auth.models import User, AnonymousUser
from django.shortcuts import get_object_or_404


# Create your tests here.
class TestLoginViews(TestCase):

    def test_get_login_page(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_can_log_in(self):
        user1 = User.objects.create_user(
            username='testUser',
            email='testUser@example.com',
            password='passw0rd')

        response = self.client.get('/books/')
        self.assertEqual(response.context['user'], AnonymousUser())

        response = self.client.post("/accounts/login", {
            'username': 'testUser',
            'password': 'pass0word'
        })

        response = self.client.get('/accounts/login')


class TestLogoutView(TestCase):

    def test_logout_form(self):
        response = self.client.get("/accounts/logout")
        self.assertRedirects(response, '/')


class TestRegisterView(TestCase):

    def test_get_register_page(self):
        response = self.client.get('/accounts/register')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')

    # def test_user_does_not_exist(self):
    #     response = self.client.post("/accounts/login", {
    #         'username': 'testUser',
    #         'password': 'pass0word'
    #     })
    #     self.assertContains(response, 'Incorrect username or password!'

    # def testLogin_get_profile_page(self):
    #   self.client.login(username='john', password='johnpassword')
    #   response = self.client.get('/accounts/profile/')
    #   self.assertEqual(response.status_code, 200)
    #   self.assertTemplateUsed(response, 'accounts/profile.html')
