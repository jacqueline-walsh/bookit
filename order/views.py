from django.shortcuts import render, get_object_or_404
from .models import Order, OrderItem
from django.contrib.auth.decorators import login_required

# Create your views here.
def thanks(request, order_id):
  if order_id:
    customer_order = get_object_or_404(Order, id=order_id)
  return render(request, 'order/thanks.html', {'customer_order': customer_order})

# View individual order history
def viewOrder(request, order_id):
  if request.user.is_authenticated:
    email = str(request.user.email)
    order = Order.objects.get(id=order_id, emailAddress=email)
    order_items = OrderItem.objects.filter(order=order)
    context =  {'order': order, 'order_items': order_items}
  return render(request, 'order/order_details.html', context)