from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.lis_clientes, name='list_clientes'),
    path('ventas/', views.lis_venta, name='list_ventas'),
    path('empleados/', views.lis_empleado, name='list_empleados'),
    path('area/', views.lis_area, name='list_area'),
]