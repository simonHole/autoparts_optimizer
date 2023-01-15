from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render, redirect
from parts import views


def index(request):
    if request.user.is_superuser:
        return redirect('admin/')

    return render(request, 'index.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('parts/', include('parts.urls')),

    path('cars/', views.show_marks, name='show_marks'),
    path('', index, name='index')
]
