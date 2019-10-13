from django.urls import path
from . import views

urlpatterns = [
  path('', views.books, name="books"),
  path('book/<int:book_id>', views.book, name='book'),  
]