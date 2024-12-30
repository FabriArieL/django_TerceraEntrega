from django.db import models

class Moto(models.Model):
    marca = models.CharField(max_length=20)
    anio = models.IntegerField()
    modelo = models.CharField(max_length=20)
    
    def __str__(self):
        return f"Moto ({self.id}): {self.marca} - {self.anio} - {self.anio}"
    
