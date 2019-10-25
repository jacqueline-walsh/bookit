from datetime import datetime
from django.db import models
from authors.models import Author

# Create your models here.
class Books(models.Model):
  author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
  title = models.CharField(max_length=200)
  isbn = models.CharField(max_length=200)
  description = models.TextField()
  price = models.DecimalField(max_digits=5, decimal_places=2)
  category_name = models.CharField(max_length=200)
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  is_published = models.BooleanField(default=True)
  stock = models.IntegerField()
  available = models.BooleanField(default=True)
  list_date = models.DateTimeField(default=datetime.now, blank=True)
  stock = models.IntegerField(default=0)
  available = models.BooleanField(default=True)
  updated = models.DateTimeField(auto_now=True)
  def __str__(self):
    return self.title
