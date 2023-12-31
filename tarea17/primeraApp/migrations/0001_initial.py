# Generated by Django 4.2.7 on 2023-11-12 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_del_area', models.CharField(max_length=100)),
                ('descripcion', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('edad', models.PositiveIntegerField()),
                ('dui', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField()),
                ('apellido', models.CharField()),
                ('edad', models.PositiveIntegerField()),
                ('areaId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='primeraApp.area')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_venta', models.DateTimeField()),
                ('monto', models.FloatField()),
                ('clienteId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='primeraApp.cliente')),
                ('empleadoId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='primeraApp.empleado')),
            ],
        ),
    ]
