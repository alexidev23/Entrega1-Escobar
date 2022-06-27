from django.db import models

# Create your models here.
class Profesores(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    correo = models.EmailField()
    salario = models.IntegerField()

    def __str__(self):
        return f"nombre:{self.nombre} - apellido: {self.apellido} - edad: {self.edad} - correo: {self.correo} - salario: {self.salario}"

class Cursos(models.Model):
    curso = models.CharField(max_length=40)
    dia = models.CharField(max_length=40)
    hora = models.CharField(max_length=40)
    costo = models.IntegerField()

    def __str__(self):
        return f"curso:{self.curso} - dia: {self.dia} - hora: {self.hora} - costo: {self.costo}"

class Alumnos(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    correo = models.EmailField()

    def __str__(self):
        return f"nombre:{self.nombre} - apellido: {self.apellido} - edad: {self.edad} - correo: {self.correo}"
