from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', index, name='index'),

    path('', include('users.urls')),
    path('', include('parts.urls')),
    path('orders/', include('orders.urls')),
]
