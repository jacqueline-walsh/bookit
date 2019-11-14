from django.test import SimpleTestCase
from django.urls import reverse, resolve
from cart.views import cart_detail


class TestUrls(SimpleTestCase):

  def test_cart_detail_url_is_resolved(self):
    url = reverse('cart:cart_detail')
    self.assertEqual(resolve(url).func, cart_detail)
