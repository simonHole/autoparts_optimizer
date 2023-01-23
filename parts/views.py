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
    select_part = Part.objects.get(id=part)

    # When product is original
    if select_part.is_original:
        substitutes = Part.objects.filter(original_id=part)

        # Context for original product article
        context = {
            'select_part': select_part,
            'substitutes': substitutes
        }

    else:
        original_identify = select_part.original_id
        substitutes = Part.objects.filter(
            original_id=original_identify.id).exclude(id=part)

        all = substitutes.union(Part.objects.filter(
            id=substitutes[0].original_id.id))

        context = {
            'select_part': select_part,
            'original_identify': original_identify
        }

    # Context for

    return render(request, 'parts/part.html', context)
