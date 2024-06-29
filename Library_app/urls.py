from django.urls import path
from . import views
from .views import index, libros, busqueda_resultados

urlpatterns = [
    path('', index, name="index"),
    path('libros/', libros, name="libros"),
    path('busqueda_resultados/', views.busqueda_resultados, name="busqueda_resultados"),
]