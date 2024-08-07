import requests
from django.shortcuts import render, redirect, get_object_or_404, redirect
from .models import Producto, TipoLibro, Carrito
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from .forms import ProductoForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from datetime import datetime
from django.db.models import Q

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
    tipo_libro = TipoLibro.objects.get(tipo='Libro')  
    productos = Producto.objects.filter(tipolibro=tipo_libro)
    
    query = request.GET.get('q')
    if query:
        productos = productos.filter(
            Q(titulo__icontains=query) | Q(autor__icontains=query)
        )
        
    data = {
        'productos': productos,
        'query': query  # Pasar el término de búsqueda a la plantilla
    }
    return render(request, 'app/libros.html', data)

@login_required
def comics(request):
    tipo_libro = TipoLibro.objects.get(tipo='Comics')
    productos = Producto.objects.filter(tipolibro=tipo_libro)
    
    query = request.GET.get('q')
    if query:
        productos = productos.filter(
            Q(titulo__icontains=query) | Q(autor__icontains=query)
        )
    
    data = {
        'productos': productos,
        'query': query  # Pasar el término de búsqueda a la plantilla
    }
    return render(request, 'app/comics.html', data)

@login_required
def mangas(request):
    tipo_libro = TipoLibro.objects.get(tipo='Manga')
    productos = Producto.objects.filter(tipolibro=tipo_libro)
    
    query = request.GET.get('q')
    if query:
        productos = productos.filter(
            Q(titulo__icontains=query) | Q(autor__icontains=query)
        )
    
    data = {
        'productos': productos,
        'query': query  # Pasar el término de búsqueda a la plantilla
    }
    return render(request, 'app/mangas.html', data)

@permission_required('Library_app.add_producto')
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
def cart(request, mostrar_confirmacion=False):
    productos_en_carrito = Carrito.objects.all()
    total_carrito = 0
    for item in productos_en_carrito:
        subtotal = item.producto.precio * item.cantidad
        total_carrito += subtotal
        item.subtotal = subtotal  # Agregamos subtotal al objeto para usar en la plantilla
    
    data = {
        'productos_en_carrito': productos_en_carrito,
        'total_carrito': total_carrito,
        'mostrar_confirmacion': mostrar_confirmacion  # Pasar mostrar_confirmacion al contexto
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
def eliminar_todo_del_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
    # Eliminar todos los productos del carrito para este tipo de producto
    Carrito.objects.filter(producto=producto).delete()
    
    messages.success(request, f'Se elimino "{producto.titulo}" del carrito.')
    return redirect('cart')

@login_required
def pagar(request):
    # Eliminar todos los productos del carrito
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
@permission_required('Library_app.view_producto')
def adminList(request):
        productos = Producto.objects.all()

        data = {
                'productos': productos
        }


        return render(request, 'app/adminList.html', data)
@permission_required('Library_app.upgrade_producto')
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
@permission_required('Library_app.delete_producto')
def adminDelete(request, id):
        producto = get_object_or_404(Producto, id=id)
        producto.delete()
        return redirect(to="adminList")
