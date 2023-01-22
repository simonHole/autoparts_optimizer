from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.show_marks, name='show_marks'),
    path('models/<str:mark>', views.show_models, name='show_models'),
    path('engines/<str:model>', views.show_engines, name='show_engines'),
    path('parts/<str:engine>', views.show_parts, name='show_parts'),
    path('part/<str:part>', views.show_part, name='show_part')
]
