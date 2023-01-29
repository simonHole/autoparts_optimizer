from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.orders, name='orders'),
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/<str:part>', views.add_to_cart, name='add_to_cart')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
