# from django.test import TestCase

# # Create your tests here.
# class TestCartViewLoggedOut(TestCase):
#     """ Test for cart view when user is logged out """

#     def setUp(self):
#         self.client = Client()

#     def test_response_redirect(self):
#         """ checks that user not logged in is redirected to login page """

#         response = self.client.get('/cart/')
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(response.url, "/accounts/login/?next=/cart/")


# class TestCartViewLoggedIn(TestCase):
#     """ Tests for cart view when user is logged in """

#     def setUp(self):
#         """ Creates instance of user in test database so login status can be achieved """
#         self.factory = RequestFactory()
#         self.user = User.objects.create_user(
#             username='testuser', email='test@email.com', password="testing321"
#         )
    
#     def test_response_status_200(self):
#         """ Test that Logged in user is not redirected from cart page """

#         client = Client()
#         client.login(username='testuser', password="testing321")

#         response = client.get('/cart/')
#         self.assertEqual(response.status_code, 200)

#     def test_load_page_with_no_cart_contents(self):
#         """ Test that view context includes nothing_in_cart set to true when page loaded with no cart items in session """

#         client = Client()
#         client.login(username='testuser', password="testing321")

#         response = client.get('/cart/')
#         context = response.context
#         self.assertTrue(context['nothing_in_cart'])