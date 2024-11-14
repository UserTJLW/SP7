from django.contrib.auth.models import User
from django.db import models

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)  # Relación uno a uno con el usuario
    customer_name = models.CharField(max_length=100)
    customer_surname = models.CharField(max_length=100)
    customer_DNI = models.CharField(max_length=20)
    dob = models.DateField(null=True, blank=True)
    branch_id = models.ForeignKey('sucursal.Sucursal', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.customer_name} {self.customer_surname}"


