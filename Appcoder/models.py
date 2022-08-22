from django.db import models

class Madre(models.Model):
    nombre=models.CharField(max_length=50)
    dni=models.ImageField()
    fecha_nacimiento=models.DateField()

class Sobrino(models.Model):
    nombre=models.CharField(max_length=50)
    email=models.EmailField()
    fecha_nacimiento=models.DateField()

class Sobrina(models.Model):
    nombre=models.CharField(max_length=50)
    colegio=models.CharField(max_length=50)
    examenes=models.ImageField()


    

