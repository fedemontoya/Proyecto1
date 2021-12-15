from django.db import models

# Create your models here.
class Autos(models.Model):

    marca = models.CharField(max_length=40)
    modelo = models.IntegerField()
    tipo = models.CharField(max_length=40)
    entregado = models.BooleanField()

    def __str__(self):
        return f"Marca: {self.marca} Modelo: {self.modelo} Tipo: {self.tipo} Entregado: {self.entregado}"

class Inmuebles(models.Model):

    direccion = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=40)
    anio = models.IntegerField()
    def __str__(self):
        return f"Direccion: {self.direccion} Ciudad: {self.ciudad} Año: {self.anio}"

class Facultad(models.Model):

    anio = models.IntegerField()
    carrera = models.CharField(max_length=40)
    universidad = models.CharField(max_length=40)
    email = models.EmailField(default='')

    def __str__(self):
        return f"Año: {self.anio} Carrera: {self.carrera} Universidad: {self.universidad} Email: {self.email}"