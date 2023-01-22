from django.core import paginator
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Car, Engine, Part


def show_marks(request):
    cars = set(car.mark for car in Car.objects.all())

    context = {
        'cars': cars
    }

    return render(request, 'parts/marks.html', context)


def show_models(request, mark):
    mark_cars = Car.get_models(mark.upper())

    context = {
        'mark_cars': mark_cars
    }

    return render(request, 'parts/models.html', context)


def show_engines(request, model):
    engines = Engine.objects.filter(car_id=model)

    context = {
        'engines': engines
    }

    return render(request, 'parts/engines.html', context)


def show_parts(request, engine):
    parts = Part.objects.filter(engine_id=engine)

    context = {
        'parts': parts
    }
    return render(request, 'parts/parts.html', context)


def show_part(request, part):
    part = Part.objects.get(id=part)

    context = {
        'part': part
    }

    return render(request, 'parts/part.html', context)
