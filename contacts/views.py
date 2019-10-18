from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

# Create your views here.
def contact(request):
  if request.method == 'POST':
    book_id = request.POST['book_id']
    book = request.POST['book']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']

    # Check if user has made contact for book already
    if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = Contact.objects.all().filter(book_id=book_id, user_id=user_id)
      if has_contacted:
        messages.error(request, 'You have already contacted us about this book, we will be back to you soon')
        return redirect('/books/book/'+book_id) 

    contact = Contact(book=book, book_id=book_id, name=name, email=email, 
    phone=phone, message=message, user_id=user_id)

    contact.save()

    # send email
    send_mail(
      'Book Enquiry',
      'A request for more information about,  ' + book + '.  Sign into the admin panel for more information',
      'jacqueline.walsh34@gmail.com',
      ['jacqueline.walsh34@gmail.com'],
      fail_silently=False
    )

    messages.success(request, 'Thank you for contacting us, will get back to you shortly')

    return redirect('/books/book/'+book_id) 