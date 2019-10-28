from django import forms


class LoginForm(forms.Form):
  username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))

class RegisterForm(forms.Form):
  first_name = forms.CharField(max_length=20, min_length=2, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
  last_name = forms.CharField(max_length=20, min_length=2, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
  username = forms.CharField(max_length=20, min_length=6, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
  email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"class": "form-control"}))
  password = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput(attrs={"class": "form-control"}))
  password_confirm = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput(attrs={"class": "form-control"}))