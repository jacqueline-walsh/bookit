from django.shortcuts import render

# Create your views here.
# return all Books
def books(request):
  return render(request, 'books/books.html')

# return single book
def book(request, book_id):
  return render(request, 'books/book.html')