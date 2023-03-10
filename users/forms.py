from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Client


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='Użytkownik')
    password = forms.CharField(widget=forms.PasswordInput, label="Hasło")


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email',
                  'username', 'password1', 'password2']
        labels = {
            'first_name': 'Imię',
            'last_name': 'Nazwisko',
            'email': 'Adres e-mail'
        }

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class EditClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'surname', 'email', 'image']
        labels = {
            'name': 'Imię',
            'surname': 'Nazwisko',
            'email': 'Adres e-mail',
            'image': 'Obraz profilowy'
        }

        def __init__(self, *args, **kwargs):
            super(EditClientForm, self).__init__(*args, **kwargs)

            for key, value in self.fields.items():
                value.widget.attrs.update({'class': 'input'})
