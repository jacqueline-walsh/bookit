from django.test import TestCase


# Create your tests here.
class TestAccountsViews(TestCase):

  def test_get_home_page(self):
    response = self.client.get('/')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'pages/index.html')

  def test_get_about_page(self):
    response = self.client.get('/about/')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'pages/about.html')