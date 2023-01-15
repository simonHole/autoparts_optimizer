from django.urls import path
from . import views

urlpatterns = [
    path('', views.parts, name='parts'),
    path('<str:pk>/', views.part, name='part'),
]
