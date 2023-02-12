from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders, name='orders'),
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/<str:part>', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout, name='checkout'),
]
