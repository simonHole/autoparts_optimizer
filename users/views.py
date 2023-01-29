from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages

from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm


def user_login(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username').lower()
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return redirect('login')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


def user_register(request):
    page = 'register'
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'Rejestracja przebiegła pomyślnie.')

            login(request, user)
            return redirect('index')

        else:
            messages.success(
                request, 'Błąd podczas rejestracji.')

    context = {'page': page, 'form': form}
    return render(request, 'users/register.html', context)


@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('index')


def user_about(request):
    user = User.objects.get(username=request.user.username)
    context = {
        'user': user
    }

    return render(request, 'users/about.html', context)
