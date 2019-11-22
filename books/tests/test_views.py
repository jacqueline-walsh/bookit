from django.test import TestCase
from books.models import Books
from authors.models import Author


# Create your tests here.


class TestAccountsViews(TestCase):

    def test_get_books_page(self):
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/books.html')

    def test_get_book_page(self):
        author = Author(name="Test author name", photo="test.jpg")
        author.save()
        book = Books(title="Test for book", price=9.99,
                     author_id=author.id, photo_main="test.jpg")
        book.save()

        response = self.client.get("/books/book/1")
        self.assertEqual(response.status_code, 200)
    

    def test_get_search_page(self):
        response = self.client.get('/books/search')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/search.html')


# Helper functions
def get_names(templates):
    names = []
    for t in templates:
        names.append(t.name)
    return names
