from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
  path('register', views.register, name='register'),  
  path('login/', views.login, name="login"),
  path('profile/', views.profile, name="profile"),
  path('logout', views.logout, name='logout'),

# Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
  path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
      name='password_change'),

  path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
      name='password_change_done'),

  path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

  path('password_reset_done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
    name='password_reset_done'),

  path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

  path('reset_done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
    name='password_reset_complete'),
]