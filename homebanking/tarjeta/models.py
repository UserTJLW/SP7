from django.db import models
from cliente.models import Cliente

class Marca(models.Model):
    id_marca = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

class Tarjeta(models.Model):
    id_tarjeta = models.AutoField(primary_key=True)
    numero = models.CharField(max_length=20)
    cvv = models.CharField(max_length=3)
    fecha_otorgamiento = models.DateField()
    fecha_expiracion = models.DateField()
    tipo_tarjeta = models.CharField(max_length=50)
    customer = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
