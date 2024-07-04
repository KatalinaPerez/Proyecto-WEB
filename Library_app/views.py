import requests
from django.shortcuts import render, redirect, get_object_or_404, redirect
from .models import Producto, TipoLibro, Carrito
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from .forms import ProductoForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Create your views here.
def get_time(request):
    try:
        response = requests.get('http://worldtimeapi.org/api/timezone/America/Santiago')
        response.raise_for_status()  # Asegura que la solicitud fue exitosa
        data = response.json()
        current_time = data['datetime']
        # Convertir la hora a un formato legible
        formatted_time = datetime.strptime(current_time, '%Y-%m-%dT%H:%M:%S.%f%z').strftime('%Y-%m-%d %H:%M:%S')
        return JsonResponse({'current_time': formatted_time})
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
    except ValueError as e:
        return JsonResponse({'error': 'Error parsing date: ' + str(e)}, status=500)
        
def index(request):
	productos =Producto.objects.all()
	data = {
		'productos': productos
	}
	return render(request, 'app/index.html', data)

@login_required
def libros(request):
        try:
                tipo_libro = TipoLibro.objects.get(tipo='Libro')  # Obtener el objeto TipoLibro con tipo 'Libro'
                productos = Producto.objects.filter(tipolibro=tipo_libro)  # Filtrar productos por tipo 'Libro'
        except TipoLibro.DoesNotExist:
                productos = Producto.objects.none()  # No hay productos si no existe el tipo 'Libro'
        
        data = {
                'productos': productos
        }
        return render(request, 'app/libros.html', data)
@login_required
def comics(request):
        try:
                tipo_libro = TipoLibro.objects.get(tipo='Comics')  # Obtener el objeto TipoLibro con tipo 'Libro'
                productos = Producto.objects.filter(tipolibro=tipo_libro)  # Filtrar productos por tipo 'Libro'
        except TipoLibro.DoesNotExist:
                productos = Producto.objects.none()  # No hay productos si no existe el tipo 'Libro'
        
        data = {
                'productos': productos
        }
        return render(request, 'app/comics.html', data)
@login_required
def mangas(request):
        try:
                tipo_libro = TipoLibro.objects.get(tipo='Manga')  
                productos = Producto.objects.filter(tipolibro=tipo_libro) 
        except TipoLibro.DoesNotExist:
                productos = Producto.objects.none()  
        
        data = {
                'productos': productos
        }
        return render(request, 'app/mangas.html', data)

@login_required
def adminAdd(request):

        data = {
                'form': ProductoForm()
        }
        if request.method == 'POST':
                formulario = ProductoForm(data=request.POST, files=request.FILES)
                if formulario.is_valid():
                        formulario.save()
                        data["mensaje"] = "Guardado Correctamente"
                else:
                        data["form"] = formulario
        return render(request, 'app/adminAdd.html', data)

@login_required
def cart(request):
    productos_en_carrito = Carrito.objects.all()
    total_carrito = 0
    for item in productos_en_carrito:
        subtotal = item.producto.precio * item.cantidad
        total_carrito += subtotal
        item.subtotal = subtotal  # Agregamos subtotal al objeto para usar en la plantilla
    
    data = {
        'productos_en_carrito': productos_en_carrito,
        'total_carrito': total_carrito,
    }
    return render(request, 'app/cart.html', data)

@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, created = Carrito.objects.get_or_create(producto=producto)

    if not created:
        carrito.cantidad += 1
    else:
        carrito.cantidad = 1  # Si se crea por primera vez, establecer cantidad en 1

    carrito.save()
    messages.success(request, 'Se agregó al carrito!')
    # Redirigir a la página anterior (libros.html)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def eliminar_del_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
    # Obtener el objeto del carrito para el producto actual
    carrito = Carrito.objects.filter(producto=producto).first()
    
    if carrito:
        if carrito.cantidad > 1:
            carrito.cantidad -= 1
            carrito.save()
            messages.success(request, f'Se disminuyó la cantidad de "{producto.titulo}" en el carrito.')
        else:
            carrito.delete()
            messages.success(request, f'Se eliminó "{producto.titulo}" del carrito.')
    else:
        messages.error(request, 'El producto no está en su carrito.')

    return redirect('cart')

@login_required
def pagar(request):
    
    Carrito.objects.all().delete()
    messages.success(request, 'Compra realizada con éxito!')
    return redirect('cart')

def registro(request):
        data = {
                'form': CustomUserCreationForm()
        }
        if request.method == 'POST':
                formulario = CustomUserCreationForm(data=request.POST)
                if formulario.is_valid():
                        formulario.save()
                        user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
                        login(request, user)

                        return redirect(to="index")
                data["form"] = formulario
        return render(request, 'registration/registro.html', data)
@login_required
def adminList(request):
        productos = Producto.objects.all()

        data = {
                'productos': productos
        }


        return render(request, 'app/adminList.html', data)
@login_required
def adminUp(request, id):

        producto = get_object_or_404(Producto, id=id)
        
        data = {
                'form' : ProductoForm(instance=producto)
         }

        if request.method == 'POST':

                formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
                if formulario.is_valid():
                        formulario.save()
                        return redirect(to="adminList")
                data["form"] = formulario

        return render(request, 'app/adminUp.html', data)
@login_required
def adminDelete(request, id):
        producto = get_object_or_404(Producto, id=id)
        producto.delete()
        return redirect(to="adminList")