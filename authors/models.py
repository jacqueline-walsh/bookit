from django.db import models
from datetime import datetime


# Create your models here.
class Author(models.Model):
  name = models.CharField(max_length=200)
  photo = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=True)
  description = models.TextField(blank=True)
  is_author_of_month = models.BooleanField(default=False)
  def __str__(self):
    return self.name
