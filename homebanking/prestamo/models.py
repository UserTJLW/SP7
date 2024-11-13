from django.db import models
from cliente.models import Cliente

class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.CharField(max_length=50)
    loan_date = models.DateField()
    loan_total = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.ForeignKey(Cliente, on_delete=models.CASCADE)
