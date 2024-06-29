from django.shortcuts import render
from django.http import JsonResponse
from .models import Libros
import json
from django.views.decorators.csrf import csrf_exempt
import logging

# Create your views here.

def home(request):
	return render(request, 'app/home.html')

def index(request):
	return render(request, 'app/index.html')

def libros(request):
	return render(request, 'app/libros.html')

def guardar_libro(request):
    # msje función está siendo llamada
    logging.debug('Llamada a la vista guardar_libro')

    # Le asigno los valores obtenidos con fetch
    if request.method == 'POST':
        data = json.loads(request.body)
        titulo = data.get('titulo', '')
        autor = data.get('autor', '')
        portada = data.get('portada', '')

        # Añade mensajes de logging para verificar los datos recibidos
        logging.debug(f'Título: {titulo}, Autor: {autor}, Portada: {portada}')

        # Crear un nuevo objeto Libros y guardarlo en la base de datos
        nuevo_libro = Libross.objects.create(
            titulo=titulo,
            autor=autor,
            portada=portada
        )

        # Añade un mensaje de logging para confirmar que se guardó el libro
        logging.debug('Libro guardado correctamente en la base de datos')

        return JsonResponse({'message': 'Libro guardado correctamente.'})
    else:
        return JsonResponse({'error': 'Método no permitido.'}, status=405)
