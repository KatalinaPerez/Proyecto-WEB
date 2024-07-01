from django.shortcuts import render
from .models import Producto

# Create your views here.

def home(request):
        return render(request, 'app/home.html')

def mangas(request):
        return render(request, 'app/mangas.html')


def comics(request):
        productos = Producto.objects.all()
        data = {
                'productos': productos
        }
        return render(request, 'app/comics.html',data)