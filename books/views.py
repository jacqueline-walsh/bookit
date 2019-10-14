from django.shortcuts import render
from books.models import Books
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
  return render(request, 'books/book.html')