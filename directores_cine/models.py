from django.db import models

# Create your models here.


class Director(models.Model):
    nombre = models.CharField(max_length=30, null=False)
    apellido = models.CharField(max_length=30, null=False)
    fecha_nacimiento = models.DateField(null=False)
    nacionalidad = models.CharField(max_length=20, null=False)

    def __str__(self) -> str:
        return f'Director {self.id}: {self.nombre}, {self.apellido}'


class Pelicula(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    descripcion = models.TextField(
        max_length=1000, null=False, help_text="La descripcion de la pelicula")
    fecha_estreno = models.DateField(null=False)
    duracion_minutos = models.IntegerField(null=False)
    director = models.ForeignKey(
        Director, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f'Pelicula {self.id}: {self.titulo}'