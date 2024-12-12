from django.db import models

class Celular(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    anio = models.IntegerField()

    def __str__(self):
        return f"Celular({self.id}): {self.marca} - {self.modelo}"