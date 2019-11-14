from django.test import SimpleTestCase
from django.urls import reverse, resolve
from books.views import books, book, search


class TestUrls(SimpleTestCase):

    def test_books_url_is_resolved(self):
        url = reverse('books')
        self.assertEqual(resolve(url).func, books)

    def test_book_url_is_resolved(self):
        url = reverse('book', args=[5])
        self.assertEqual(resolve(url).func, book)

    def test_search_url_is_resolved(self):
        url = reverse('search')
        self.assertEqual(resolve(url).func, search)

