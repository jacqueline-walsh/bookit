from django.contrib import admin
from authors.models import Author

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'is_author_of_month')
  list_editable = ('is_author_of_month',)
  list_display_links = ('id', 'name')
  search_fields = ('name',)
  list_per_page = 25

admin.site.register(Author, AuthorAdmin)
