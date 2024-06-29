from django.db import models
import random

#Generar precios random
def precio_random():
    return random.randint(3, 15) * 1000

class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    portada = models.ImageField(upload_to="Libros, null=True")
    precio = models.IntegerField(default=precio_random)

    def __str__(self):
        return self.titulo

#class Carrito(models.Model):
 #   titulo = models.CharField(max_length=255)
  #  autor = models.CharField(max_length=255)
   # imagen_url = models.ImageField()
    #precio = models.CharField(max_length=50)

#    def __str__(self):
 #       return self.titulo