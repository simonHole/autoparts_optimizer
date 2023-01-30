from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Order, OrderItem, Client
from parts.models import Part


# Create your views here.


def orders(request):
    if request.uster.is_authenticated:
        pass

    context = {

    }
    return render(request, 'orders/cart.html', context)


@login_required(login_url='index')
def cart(request):
    if request.user.is_authenticated:
        client = Client.objects.get(user=request.user)
        order, created = Order.objects.get_or_create(
            client=client, complete=False)
        items = order.orderitem_set.all()
    else:
        return redirect('inex')

    context = {
        'order': order,
        'items': items
    }
    return render(request, 'orders/cart.html', context)


@login_required(login_url='index')
def checkout(request):
    if request.user.is_authenticated:
        client = Client.objects.get(user=request.user)
        order, created = Order.objects.get_or_create(
            client=client, complete=False)
        items = order.orderitem_set.all()
    else:
        return redirect('inex')

    context = {
        'order': order,
        'items': items
    }
    return render(request, 'orders/checkout.html', context)


@login_required(login_url='index')
def add_to_cart(request, part):
    part = Part.objects.get(id=part)

    context = {
        'part': part
    }

    return render(request, 'orders/add-to-cart.html', context)
