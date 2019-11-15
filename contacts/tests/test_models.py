from django.test import TestCase
from contacts.models import Contact

# Create your tests here.
class TestAuthorModel(TestCase):

  def test_can_create_contact_message(self):
    contact = Contact(book_id=1, book="Test book title", user_id=1, message="Test message")
    contact.save()
    self.assertEqual(contact.message, "Test message")


