from django.db import models

# Create your models here.
class Usuario(models.Model):
    id = models.IntegerField (primary_key = True, verbose_name = 'Id de Usuario') #verbosename es lo que sale como un label en lapaginas
    nombre = models.CharField (max_length = 20, verbose_name = 'Nombre usuario')
    
    def __str__(self): # metodo toString
        return self.nombre

class Admin(models.Model):
    cargo = models.CharField(max_length = 7, primary_key = True, verbose_name = 'Cargo Admin')
    id = models.ForeignKey (Usuario, on_delete=models.CASCADE) #se da relacion con usuario

    def __str__(self):
        return self.cargo