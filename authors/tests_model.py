from django.test import TestCase
from .models import Author

# Create your tests here.
class TestAuthorModel(TestCase):

  def test_author_of_month_defaults_to_False(self):
    author = Author(name="Test author name")
    author.save()
    self.assertEqual(author.name, "Test author name")
    self.assertFalse(author.is_author_of_month)

  def test_can_create_an_author_with_a_name_and_status(self):
    author = Author(name="Test author name", is_author_of_month=True)
    author.save()
    self.assertEqual(author.name, "Test author name")
    self.assertTrue(author.is_author_of_month)


