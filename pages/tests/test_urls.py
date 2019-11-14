from django.test import SimpleTestCase
from django.urls import reverse, resolve
from pages.views import index, about


class TestUrls(SimpleTestCase):

  def test_index_url_is_resolved(self):
    url = reverse('index')
    self.assertEqual(resolve(url).func, index)

  def test_about_url_is_resolved(self):
    url = reverse('about')
    self.assertEqual(resolve(url).func, about)