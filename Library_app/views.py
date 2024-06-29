from django.shortcuts import render
from .models import Libro

# Create your views here.

def index(request):
	return render(request, 'app/index.html')

def libros(request):
	libros =Libro.objects.all()
	data = {
		'libros': libros
	}
	return render(request, 'app/libros.html', data)

def busqueda_resultados(request):
    query = request.GET.get('q')

    if query:
        libros = Libro.objects.filter(titulo__icontains=query) | Libro.objects.filter(autor__icontains=query)
    else:
        libros = Libro.objects.all()

    context = {
        'libros': libros,
        'query': query,
    }
    return render(request, 'busqueda_resultados.html', context)
