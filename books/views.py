from django.shortcuts import render, get_object_or_404
from books.models import Books
from authors.models import Author
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
# return all books paginated to 6 on a page
def books(request):
  books = Books.objects.order_by('-list_date').filter(is_published=True)
  paginator = Paginator(books, 6)
  page = request.GET.get('page')
  paged_books = paginator.get_page(page)

  context = { 'books': paged_books }
  return render(request, 'books/books.html', context)

# return a single book
def book(request, book_id):
  book = get_object_or_404(Books, pk=book_id)
  authors = book.author
  author = Author.objects.all().filter(name=True)
  context = {'book': book, 'author': 'author'}
  return render(request, 'books/book.html', context)

# search
def search(request):
  return render(request, 'books/search.html')
