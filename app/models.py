from django.db import models

# Create your models here.

class TipoLibro(models.Model):
    tipo = models.CharField(max_length=50)
    
    def __str__(self):
        return self.tipo



class Producto(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    portada = models.ImageField(upload_to="productos", null=True)
    precio = models.IntegerField()
    categoria = models.CharField(max_length=60)
    tipolibro= models.ForeignKey(TipoLibro, on_delete=models.PROTECT)

    def __str__(self):
        return self.titulo

