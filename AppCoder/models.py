from django.db import models

# Create your models here.
class autos(models.Model):

    marca = models.CharField(max_length=40)
    modelo = models.IntegerField()
    tipo = models.CharField(max_length=40)
    entregado = models.BooleanField(default=True)

class inmuebles(models.Model):

    direccion = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=40)
    anio = models.IntegerField()

class facultad(models.Model):

    anio = models.IntegerField()
    carrera = models.CharField(max_length=40)
    universidad = models.CharField(max_length=40)
    email = models.EmailField(default='')