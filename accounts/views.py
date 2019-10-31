from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm
from order.models import Order, OrderItem
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
  form = RegisterForm()
  if request.method == 'POST':
    # get form values
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']   
    username = request.POST['username']   
    email = request.POST['email']   
    password = request.POST['password']     
    password_confirm = request.POST['password_confirm']  
    # check if passwords match
    if password == password_confirm:
      # check username not already used
      if User.objects.filter(username=username).exists():
        messages.error(request, 'That username already exists')
        return redirect('register') 
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request, 'That email already exists')
          return redirect('register') 
        else: 
          user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password
          ) 
          # ---- Login in directly after registration ----
          auth.login(request, user)
          messages.success(request, "You have succesfully registered and are now logged in")
          return redirect('index')
    else:
      messages.error(request, 'passwords do not match')
      return redirect('register')
  else:
    return render(request, 'accounts/register.html', {'form': form})


def login(request):
  form = LoginForm()
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      messages.success(request, "You are now logged in")
      return redirect('index')
    else:
      messages.error(request, "Invalid username or password")
      return redirect('login')
  else:
    return render(request, 'accounts/login.html', {'form':form})


def logout(request):
    """ Logout the user out """
    auth.logout(request)
    messages.success(request, "You have successfully been logged out!")
    return redirect('index')

@login_required()
def profile(request):
    """ The user's profile page """
    if request.user.is_authenticated:
      email = str(request.user.email)
      order_details = Order.objects.filter(emailAddress=email)
    context = {'order_details': order_details}
    return render(request, 'accounts/profile.html', context)

