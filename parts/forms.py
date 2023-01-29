from django.forms import ModelForm
from django import forms
from .models import Part, Car, Engine, Vendor


class EdigOriginalForm(ModelForm):
    class Meta:
        model = Part
        fields = ['name', 'catalog_number',
                  'quality_fac', 'time_of_delivery', 'price', 'quantity', 'image']
        labels = {
            'name': 'Nazwa produktu',
            'catalog_number': 'Numer katalogowy',
            'quality_fac': 'Jakość produktu',
            'time_of_delivery': 'Czas dostawy (dni)',
            'price': 'Cena',
            'quantity': 'Ilość dostepnych produktów',
            'image': 'Zaimportuj obraz'
        }


class EditSubstitute(ModelForm):
    class Meta:
        model = Part
        fields = ['original_id', 'name', 'catalog_number',
                  'quality_fac', 'time_of_delivery', 'price', 'quantity', 'image']
        labels = {
            'original_id': 'Identyfikator oryginału',
            'name': 'Nazwa produktu',
            'catalog_number': 'Numer katalogowy',
            'quality_fac': 'Jakość produktu',
            'time_of_delivery': 'Czas dostawy (dni)',
            'price': 'Cena',
            'quantity': 'Ilość dostepnych produktów',
            'image': 'Zaimportuj obraz'
        }
