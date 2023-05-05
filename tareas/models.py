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
    
    
class Tarea_mayo(models.Model):
    titulo = models.CharField(max_length=200)
    completado = models.BooleanField(default=False)
    

    def __str__(self):
        return self.titulo
    
class Tarea_marzo(models.Model):
    titulo = models.CharField(max_length=200)
    completado = models.BooleanField(default=False)
    

    def __str__(self):
        return self.titulo
    
class Tarea_abril(models.Model):
    titulo = models.CharField(max_length=200)
    completado = models.BooleanField(default=False)
    

    def __str__(self):
        return self.titulo    
    
class Tarea_junio(models.Model):
    titulo = models.CharField(max_length=200)
    completado = models.BooleanField(default=False)
    

    def __str__(self):
        return self.titulo       
    
class Tarea_julio(models.Model):
    titulo = models.CharField(max_length=200)
    completado = models.BooleanField(default=False)
    

    def __str__(self):
        return self.titulo        

class Tarea_agosto(models.Model):
    titulo = models.CharField(max_length=200)
    completado = models.BooleanField(default=False)
    

    def __str__(self):
        return self.titulo      

class Tarea_septiembre(models.Model):
    titulo = models.CharField(max_length=200)
    completado = models.BooleanField(default=False)
    

    def __str__(self):
        return self.titulo       

class Tarea_octubre(models.Model):
    titulo = models.CharField(max_length=200)
    completado = models.BooleanField(default=False)
    

    def __str__(self):
        return self.titulo    

class Tarea_noviembre(models.Model):
    titulo = models.CharField(max_length=200)
    completado = models.BooleanField(default=False)
    

    def __str__(self):
        return self.titulo         
    
class Tarea_diciembre(models.Model):
    titulo = models.CharField(max_length=200)
    completado = models.BooleanField(default=False)
    

    def __str__(self):
        return self.titulo      