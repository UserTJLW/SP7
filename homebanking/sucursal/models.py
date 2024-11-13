from django.db import models

class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.IntegerField()
    branch_name = models.CharField(max_length=100)
    branch_address_id = models.IntegerField()  # Este campo puede ser una relación con otra tabla de direcciones si la tienes.
