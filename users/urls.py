from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='user_register'),
    path('about/', views.user_about, name='user_about'),
    path('logout', views.user_logout, name='logout'),
]
