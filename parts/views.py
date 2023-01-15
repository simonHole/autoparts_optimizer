from django.core import paginator
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Car


def part(request, pk):
    context = {
        'part_number': pk
    }

    return render(request, 'parts/single_part.html', context)


def parts(request, ):
    context = {}
    return render(request, 'parts/parts.html', context)


def show_marks(request):
    cars = Car

    context = {}
    query_cars = Car.objects.all()
    cars = set()
    for query_car in query_cars:
        cars.add(query_car.mark)

    context = {
        'cars': cars
    }

    return render(request, 'parts/cars.html', context)
