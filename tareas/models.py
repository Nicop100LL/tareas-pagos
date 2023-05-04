from django.db import models


# Create your models here.

#Crear la función tareas




class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    completado = models.BooleanField(default=False)
    

    def __str__(self):
        return self.titulo
    
class Tarea1(models.Model):
    titulo = models.CharField(max_length=200)
    completado = models.BooleanField(default=False)
   

    def __str__(self):
        return self.titulo   
    
class Tarea2(models.Model):
    titulo = models.CharField(max_length=200)
    completado = models.BooleanField(default=False)
    

    def __str__(self):
        return self.titulo    