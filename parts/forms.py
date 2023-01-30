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


class CreatePartForm(ModelForm):
    class Meta:
        model = Part
        fields = ['name', 'vendor', 'catalog_number',
                  'description', 'quality_fac', 'price', 'time_of_delivery', 'quantity', 'is_original', 'original_id', 'engine_id', 'image']
        labels = {
            'name': 'Nazwa ogłoszenia',
            'vendor': 'Producent',
            'catalog_number': 'Numer katalogowy',
            'description': 'Opis',
            'image': 'Obraz',
            'quality_fac': 'Jakość (1-100)',
            'price': 'Cena',
            'time_of_delivery': 'Czas dostawy (dni)',
            'quantity': 'Ilość',
            'is_original': 'Czy to oryginalna część?',
            'original_id': 'Numer oryginału',
            'engine_id': 'Numer silnika',
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
