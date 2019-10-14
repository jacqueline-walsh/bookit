from django.shortcuts import render
from books.models import Books
from authors.models import Author

# Create homepage
def index(request):
  books = Books.objects.filter(is_published=True).order_by('-list_date')[:3]
  context = {'books': books}
  return render(request, 'pages/index.html', context)

def about(request):
  authors = Author.objects.all()
  # get mvp
  is_author_of_month = Author.objects.all().filter(is_author_of_month=True) 
  context = {'authors' : authors, 'is_author_of_month': is_author_of_month }
  return render(request, 'pages/about.html', context)
