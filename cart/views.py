from django.shortcuts import render, redirect, get_object_or_404
from books.models import Books
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
import stripe
from django.conf import settings
from order.models import Order, OrderItem

# Create your views here.
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, book_id):
    book = Books.objects.get(id=book_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )
        cart.save(),
    try:
        cart_item = CartItem.objects.get(book=book, cart=cart)
        if cart_item.quantity < cart_item.book.stock:
            cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            book=book,
          quantity=1,
          cart=cart
        )
        cart_item.save()
    return redirect('cart:cart_detail')


def cart_detail(request, total=0, counter=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += (cart_item.book.price * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass

    ''' stripe payment details '''
    stripe.api_key = settings.STRIPE_SECRET_KEY
    stripe_total = int(total * 100)
    description = 'BookIt - Online Book Store'
    data_key = settings.STRIPE_PUBLISHABLE_KEY
    if request.method == 'POST':
      # print(request.POST)
      try:
        token = request.POST['stripeToken']
        email = request.POST['stripeEmail']
        billingName = request.POST['stripeBillingName']
        billingAddress1 = request.POST['stripeBillingAddressLine1']
        billingcity = request.POST['stripeBillingAddressCity']
        billingPostcode = request.POST['stripeBillingAddressZip']
        billingCountry = request.POST['stripeBillingAddressCountryCode']
        shippingName = request.POST['stripeShippingName']
        shippingAddress1 = request.POST['stripeShippingAddressLine1']
        shippingcity = request.POST['stripeShippingAddressCity']
        shippingPostcode = request.POST['stripeShippingAddressZip']
        shippingCountry = request.POST['stripeShippingAddressCountryCode']
        customer = stripe.Customer.create(
            email=email,
            source=token
        )
        charge = stripe.Charge.create(
            amount=stripe_total,
            currency="eur",
            description=description,
            customer=customer.id
        )
        '''Creating the order'''
        try:
          order_details = Order.objects.create(
              token=token,
              total=total,
              emailAddress=email,
              billingName=billingName,
              billingAddress1=billingAddress1,
              billingCity=billingcity,
              billingPostcode=billingPostcode,
              billingCountry=billingCountry,
              shippingName=shippingName,
              shippingAddress1=shippingAddress1,
              shippingCity=shippingcity,
              shippingPostcode=shippingPostcode,
              shippingCountry=shippingCountry
          )
          order_details.save()
          for order_item in cart_items:
            oi = OrderItem.objects.create(
              book=order_item.book.title,
              quantity=order_item.quantity,
              price=order_item.book.price,
              order=order_details
            )
            oi.save()
            '''Reduce stock when order is placed or saved'''
            books =Books.objects.get(id=order_item.book.id)
            books.stock = int(order_item.book.stock - order_item.quantity)
            books.save()
            order_item.delete()
            '''The terminal will print this message when the order is saved'''
            print('The order has been created')
          return redirect('cart:cart_detail')
        except ObjectDoesNotExist:
          pass
      except stripe.error.CardError as e:
        return False, e
    return render(request, 'cart/cart.html', dict(cart_items=cart_items, total=total, counter=counter, data_key=data_key, stripe_total=stripe_total, description=description))

def cart_remove(request, book_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    book = get_object_or_404(Books, id=book_id)
    cart_item = CartItem.objects.get(book=book, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart_detail')


def full_remove(request, book_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    book = get_object_or_404(Books, id=book_id)
    cart_item = CartItem.objects.get(book=book, cart=cart)
    cart_item.delete()
    return redirect('cart:cart_detail')
