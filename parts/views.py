from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages

from .models import Car, Engine, Part
from .forms import EdigOriginalForm, EditSubstitute, CreatePartForm


@login_required(login_url='index')
def show_marks(request):
    cars = set(car.mark for car in Car.objects.all())

    context = {
        'cars': cars
    }

    return render(request, 'parts/marks.html', context)


@login_required(login_url='index')
def show_models(request, mark):
    mark_cars = Car.get_models(mark.upper())

    context = {
        'mark_cars': mark_cars
    }

    return render(request, 'parts/models.html', context)


@login_required(login_url='index')
def show_engines(request, model):
    engines = Engine.objects.filter(car_id=model)

    context = {
        'engines': engines
    }

    return render(request, 'parts/engines.html', context)


@login_required(login_url='index')
def show_parts(request, engine):
    engine = Engine.objects.get(id=engine)
    parts = Part.objects.filter(
        Q(engine_id=engine)
    )

    context = {
        'engine': engine,
        'parts': parts
    }
    return render(request, 'parts/parts.html', context)


@login_required(login_url='index')
def show_part(request, part):

    current_part = Part.objects.filter(id=part)

    # If part is original
    if current_part[0].is_original:
        others = Part.objects.filter(original_id=current_part[0].id)
        all = others | current_part
        cheapest = Part.lowest_price(all)
        highest = Part.highetst_quality(all)
        fastest = Part.fastest_time_delivery(all)
        best_product = Part.best_product(all)

        if request.method == 'POST':
            quality = request.POST['quality']
            price = request.POST['price']
            time = request.POST['time']
            best_product = Part.best_product(all, quality, price, time)

        context = {
            'current_part': current_part[0],
            'others': others,
            'all': all,
            'cheapest': cheapest,
            'highest_quality': highest,
            'fastest_delivery': fastest,
            'best_product': best_product
        }

    # If part is one of substitutes
    else:
        original = Part.objects.filter(id=current_part[0].original_id.id)
        substitues = Part.objects.filter(
            original_id=original[0].id).exclude(id=current_part[0].id)
        others = substitues.union(original)
        all = others.union(current_part)
        cheapest = Part.lowest_price(all)
        highest = Part.highetst_quality(all)
        fastest = Part.fastest_time_delivery(all)
        best_product = Part.best_product(all)

        context = {
            'current_part': current_part[0],
            'original': original,
            'all': all,
            'others': others,
            'cheapest': cheapest,
            'highest_quality': highest,
            'fastest_delivery': fastest,
            'best_product': best_product
        }

        print(context)

    return render(request, 'parts/part.html', context)

# All admin managment views


@login_required(login_url='index')
def admin_managment(request):

    # Check if user is admin
    if request.user.is_superuser:
        originals = Part.objects.filter(original_id=None)
        context = {
            'originals': originals
        }

    # Else return to main site
    else:
        return redirect('index')

    return render(request, 'parts/admin/admin_managment.html', context)


@login_required(login_url='index')
def delete_part(request, pk):
    if request.user.is_superuser:
        part = Part.objects.get(id=pk)
        if request.method == 'POST':
            part.delete()
            messages.success(request, 'Część została usunięta pomyślnie')
            return redirect('admin-management')
    else:
        return redirect('index')

    context = {
        'part': part
    }
    return render(request, 'parts/admin/delete_part.html', context)


@login_required(login_url='index')
def add_original(request):
    if request.user.is_superuser:
        form = CreatePartForm(initial={
            'is_original': True,
            'quality_fac': 100,
            'time_of_delivery': 5,
            'price': 50,
            'quantity': 5
        })

    if request.method == 'POST':
        form = CreatePartForm(request.POST, request.FILES)
        if form.is_valid():
            part = form.save()
            return redirect('admin-management')

    context = {
        'form': form
    }

    return render(request, 'parts/admin/add-original.html', context)

# Edit original


@login_required(login_url='index')
def edit_original(request, pk):
    if request.user.is_superuser:
        part = Part.objects.get(
            Q(id=pk) or
            Q(original_id=pk)
        )
        form = EdigOriginalForm(instance=part)

        if request.method == 'POST':
            form = EdigOriginalForm(request.POST, request.FILES, instance=part)
            if form.is_valid():
                part = form.save()
                return redirect('admin-management')

        context = {
            'form': form,
            'part': part
        }

    return render(request, 'parts/admin/edit_original.html', context)

# Edit Substitute Form


@login_required(login_url='index')
def substitute(request, pk):
    if request.user.is_superuser:
        original = Part.objects.get(id=pk)
        substitutes = Part.objects.filter(original_id=pk)
        context = {
            'original': original,
            'substitutes': substitutes
        }
    else:
        return redirect('index')

    return render(request, 'parts/admin/subtitutes.html', context)


@login_required(login_url='index')
def add_substitute(request, pk):
    if request.user.is_superuser:
        original = Part.objects.get(id=pk)
        form = CreatePartForm(initial={
            'original_id': original.id,
            'engine_id': original.engine_id,
            'is_original': False,
            'quality_fac': 50,
            'time_of_delivery': 3,
            'price': 12.50,
            'quantity': 10
        })

    if request.method == 'POST':
        form = CreatePartForm(request.POST, request.FILES)
        if form.is_valid():
            part = form.save()
            return redirect('admin-management')

    context = {
        'form': form
    }

    return render(request, 'parts/admin/add-substitute.html', context)


@login_required(login_url='index')
def edit_substitute(request, pk):
    if request.user.is_superuser:
        part = Part.objects.get(
            Q(id=pk) or
            Q(original_id=pk)
        )

        original = Part.objects.get(id=part.original_id.id)
        form = EditSubstitute(instance=part)

        if request.method == 'POST':
            form = EditSubstitute(request.POST, request.FILES, instance=part)
            if form.is_valid():
                part = form.save()
                return redirect('admin-management')

        context = {
            'form': form,
            'part': part,
            'original': original
        }

    return render(request, 'parts/admin/edit_substitute.html', context)
