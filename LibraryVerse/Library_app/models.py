from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    imagen_url = models.URLField()

    def __str__(self):
        return self.titulo