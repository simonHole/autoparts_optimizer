from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='Użytkownik')
    password = forms.CharField(widget=forms.PasswordInput, label="Hasło")


class RegistrationForm(forms.Form):
    login = forms.CharField(max_length=50, label="Użytkownik")
    password = forms.CharField(widget=forms.PasswordInput, label="Hasło")
    first_name = forms.CharField(max_length=50, label="Imię")
    last_name = forms.CharField(max_length=50, label="Nazwisko")
    email = forms.EmailField(max_length=100, label="Adres e-mail")
