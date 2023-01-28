from django.shortcuts import render
from django.http import HttpResponse

from parts.models import Part

# Create your views here.


def orders(request):
    return HttpResponse('Orders View.')


def cart(request):
    context = {

    }
    return render(request, 'orders/cart.html', context)


def add_to_cart(request, part):
    part = Part.objects.get(id=part)

    context = {
        'part': part
    }

    return render(request, 'orders/add-to-cart.html', context)
