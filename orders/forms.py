from django.forms import ModelForm

from .models import ShipAddress


class SendAddress(ModelForm):
    class Meta:
        model = ShipAddress
        fields = ['zipcode', 'city', 'address', 'apartament']
        labels = {
            'city': 'Miasto',
            'zipcode': 'Kod pocztowy',
            'address': 'Ulica i numer ulicy',
            'apartament': 'Numer lokalu'
        }
