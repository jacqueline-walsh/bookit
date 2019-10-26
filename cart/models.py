from django.db import models
from books.models import Books
# Create your models here.

class Cart(models.Model):
  cart_id = models.CharField(max_length=250, blank=True)
  date_added = models.DateField(auto_now_add=True)
  
  def __str__(self):
    return self.cart_id

class CartItem(models.Model):
  book = models.ForeignKey(Books, on_delete=models.CASCADE)
  cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
  quantity = models.IntegerField()
  active = models.BooleanField(default=True)

  def sub_total(self):
    return self.book.price * self.quantity
  
  def __str__(self):
    return self.book
