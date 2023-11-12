from django.db import models

#Tabla cliente
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    dui = models.PositiveIntegerField()

#Tabla area
class Area(models.Model):
    nombre_del_area = models.CharField(max_length=100)
    descripcion = models.CharField()

#Tabla empleado
class Empleado(models.Model):
    nombre = models.CharField()
    apellido = models.CharField()
    edad = models.PositiveIntegerField()
    areaId = models.ForeignKey(Area, on_delete=models.CASCADE)

#Tabla venta
class Venta(models.Model):
    fecha_venta = models.DateTimeField()
    monto = models.FloatField()
    clienteId = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empleadoId = models.ForeignKey(Empleado, on_delete=models.CASCADE)
