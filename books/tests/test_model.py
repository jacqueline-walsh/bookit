from django.test import TestCase
from books.models import Books

# Create your tests here.
class TestBookModel(TestCase):

  def test_create_book(self):
      book = Books(title='Test Book', description='Some test content.')
      self.assertEqual(book.title, 'Test Book')
      self.assertEqual(book.description, "Some test content.")
      self.assertFalse(book.photo_main)
      self.assertFalse(book.price)
      self.assertTrue(book.available)
