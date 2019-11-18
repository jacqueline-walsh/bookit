from django.test import TestCase
from .models import Books
from authors.models import Author

# Create your tests here.
class TestAccountsViews(TestCase):

  def test_get_books_page(self):
    response = self.client.get('/books/')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'books/books.html')

  # def test_get_book_page(self):
  #   author = Author(name="Test author name")
  #   author.save()
  #   book = Books(title="Test for book", price=9.99, author_id=author.id, photo_main="photos/%Y/%m/%d/")
  #   book.save()

  #   response = self.client.get("/books/book/1")
  #   self.assertEqual(response.status_code, 200)
  #   self.assertTemplateUsed(response, "books.book.html")

  def test_get_book_page_for_book_that_does_not_exist(self):
      response = self.client.get("/books/book/0")
      self.assertEqual(response.status_code, 404)

  def test_get_search_page(self):
    response = self.client.get('/books/search')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'books/search.html')
