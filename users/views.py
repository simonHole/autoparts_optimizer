from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import LoginForm, RegistrationForm
from django.contrib.auth import logout


def user_login(request):
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

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Process the form data
            login = form.cleaned_data['login'].lower()
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            User.save()

            return redirect('index')
    else:
        form = RegistrationForm()

    return render(request, 'users/register.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('index')


def user_about(request):
    user = User.objects.get(username=request.user.username)
    context = {
        'user': user
    }

    return render(request, 'users/about.html', context)
