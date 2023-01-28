from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='Użytkownik')
    password = forms.CharField(widget=forms.PasswordInput, label="Hasło")


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User

        fields = ['first_name', 'last_name' 'email',
                  'username', 'password1', 'password2']
        labels = {
            'username': 'Nazwa użytkownika',
            'email': 'Adres e-mail',
            'first_name': 'Imię',
            'last_name': 'Nazwisko',
            'password1': 'Hasło',
            'password2': 'Powtórz hasło'
        }

        def __init__(self, *args, **kwargs):
            super(RegistrationForm, self).__init__(*args, **kwargs)

            for key, value in self.fields.items():
                value.widget.attrs.update({'class': 'input'})
