from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone
import datetime 



class Vehiculo(models.Model):
    marca = models.CharField(max_length=20, choices=[
        ["Ford", "Ford"],
        ["Chevrolet", "Chevrolet"],
        ["Fiat", "Fiat"],
        ["Toyota", "Toyota"]
    ], default="Ford")

    modelo = models.CharField(max_length = 100)
    serialCarroseria = models.CharField(max_length = 50)
    serialMotor = models.CharField(max_length = 50)
    categoria = models.CharField(max_length=20, choices=[
        ["Particular", "Particular"],
        ["Transporte", "Transporte"],
        ["Carga", "Carga"]
    ], default="Particular") 
    
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)  
    fecha_update = models.DateTimeField(auto_now=True)
    precio = models.DecimalField(max_digits=10, decimal_places=1)

    class Meta:
        permissions = (
            ("visualizar_catalogo", "Puede visualizar listado"),
            ("add_vehiculomodel", "Puede agregar vehículos"),
        )
        
    def __str__(self):
        return self.serialMotor







    







