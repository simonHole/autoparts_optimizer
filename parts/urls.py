from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.show_marks, name='show_marks'),
    path('models/<str:mark>', views.show_models, name='show_models'),
    path('engines/<str:model>', views.show_engines, name='show_engines'),
    path('parts/<str:engine>', views.show_parts, name='show_parts'),
    path('part/<str:part>', views.show_part, name='show_part'),
    path('admin-management/', views.admin_managment, name='admin-management'),

    path('delete-part/<str:pk>', views.delete_part, name='delete-part'),
    path('substitute/<str:pk>', views.substitute, name='substitute'),

    path('add-original/', views.add_original, name='add-original'),
    path('edit-original/<str:pk>', views.edit_original, name='edit-original'),

    path('edit-substitute/<str:pk>', views.edit_substitute, name='edit-substitute'),
    path('add-substitute/<str:pk>', views.add_substitute, name='add-substitute'),
]
