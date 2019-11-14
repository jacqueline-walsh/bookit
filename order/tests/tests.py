from django.test import TestCase
from django.urls import reverse, resolve
from order.views import viewOrder, thanks

# Create your tests here.
class TestUrls(TestCase):

  def test_thanks_urls_is_resolved(self):
    url = reverse('order:thanks', args=[1])
    self.assertEqual(resolve(url).func, thanks)

  def test_order_details_urls_is_resolved(self):
    url = reverse('order:order_details', args=[1])
    self.assertEqual(resolve(url).func, viewOrder)