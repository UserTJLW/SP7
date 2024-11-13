from django.db import models
from cuenta.models import Cuenta

class Movimiento(models.Model):
    movimiento_id = models.AutoField(primary_key=True)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_operacion = models.CharField(max_length=50)
    hora = models.DateTimeField(auto_now_add=True)
