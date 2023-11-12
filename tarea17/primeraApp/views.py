from django.shortcuts import render
from .models import Cliente, Venta, Empleado, Area

#funciones para visualizar las diferentes paginas que corresponden a cada tabla de datos
def lis_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})


def lis_venta(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas.html', {'ventas': ventas})


def lis_empleado(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados.html', {'empleados': empleados})


def lis_area(request):
    areas = Area.objects.all()
    return render(request, 'area.html', {'areas': areas})
