from django.urls import path
from .views import index, libros, guardar_libro

urlpatterns = [
    path('', index, name="index"),
	path('libros/', libros, name="libros"),
    path('guardar_libro/', guardar_libro, name='guardar_libro'),
]