
from django.db import models


class TipoDocumento(models.Model):
    descripcion = models.CharField(max_length=10)


class Usuario(models.Model):
    tipo_documento = models.ForeignKey(
        'TipoDocumento')
    numero_documento = models.CharField(max_length=15)
    nombre_empresa = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30, null=True)
    direccion = models.CharField(max_length=150, null=True)
    ciudad = models.CharField(max_length=100, null=True)
    celular = models.CharField(max_length=15, null=True)
    correo = models.EmailField(max_length=130, blank=True, null=True)


class Venta(models.Model):
    fecha_venta = models.DateField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=4)
    cliente = models.ForeignKey(
        'Usuario')
    serie_documento = models.CharField(max_length=16, null=True)
    tipo_documento = models.CharField(max_length=8, null=True)
    vendedor = models.ForeignKey(
        'Usuario')


# relation


class Proveedor(models.Model):
    numero_documento = models.CharField(max_length=15)
    tipodocumento = models.ForeignKey(
        'TipoDocumento', on_delete=models.DO_NOTHING, default=1)
    nombre_empresa = models.CharField(max_length=25)
    nombres = models.CharField(max_length=30, null=True)
    direccion = models.CharField(max_length=150, null=True)
    celular = models.CharField(max_length=15, null=True)
    correo = models.EmailField(max_length=130, blank=True, null=True)


class Compra(models.Model):
    fecha_compra = models.DateField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=4)
    proveedor = models.ForeignKey(
        'Proveedor')
    serie_documento = models.CharField(max_length=16, null=True)
    tipo_documento = models.ForeignKey(
        'TipoDocumento')


# realation
