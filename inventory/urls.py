from django.urls import include, path

from . import views

app_name = 'inventory'

urlpatterns = [
    path('', views.inventory_summary, name='inventory_summary'),
    path('add/', views.inventory_add, name='inventory_add'),
]
