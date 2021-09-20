from django.urls import include, path

from . import views

app_name = 'inventory'

urlpatterns = [
    path('', views.inventory_summary, name='inventory_summary'),
    path('add/', views.inventory_add, name='inventory_add'),
    path('edit/<slug:id>/', views.inventory_edit, name='inventory_edit'),
    path('inactive/<slug:id>/', views.inventory_inactive, name='inventory_inactive'),
    path('delete/<slug:id>/', views.inventory_delete, name='inventory_delete'),
]
