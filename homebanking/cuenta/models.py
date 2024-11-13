from django.db import models
from cliente.models import Cliente

class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    iban = models.CharField(max_length=34)
