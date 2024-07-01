from django.db import models
import random

#Generar precios random
def precio_random():
    return random.randint(3, 15) * 1000

class TipoLibro(models.Model):
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo

class Producto(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    portada = models.ImageField(upload_to="productos", null=True)
    precio = models.IntegerField(default=precio_random)
    categoria = models.CharField(max_length=60)
    tipolibro= models.ForeignKey(TipoLibro, on_delete=models.PROTECT)

    def __str__(self):
        return self.titulo

class Carrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    agregado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cantidad}x {self.producto.titulo}"