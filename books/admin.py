from django.contrib import admin
from books.models import Books

# Register your models here.
class BookAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'author')
  list_display_links = ('id', 'title')
  list_filter = ('author',)
  list_editable = ('is_published',)
  search_fields = ('title', 'isbn', 'category_name', 'price')
  list_per_page = 25

admin.site.register(Books, BookAdmin)

