from django.urls import path
from . import views
from .views import index, libros, comics,cart, adminAdd, eliminar_del_carrito, registro, adminList, adminUp, pagar,mangas, adminDelete

urlpatterns = [
    path('', index, name="index"),
    path('libros/', libros, name="libros"),
    #path('busqueda_resultados/', views.busqueda_resultados, name="busqueda_resultados"),
    path('comics/', comics, name="comics"),
    path('cart/', cart, name="cart"),
    path('adminAdd/', adminAdd, name="adminAdd"),
    path('agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('cart/eliminar/<int:producto_id>/', eliminar_del_carrito, name="eliminar_del_carrito"),
    path('registro/', registro, name="registro"),
    path('adminList/', adminList, name="adminList"),
    path('adminUp/<id>/', adminUp, name="adminUp"),
    path('cart/pagar/', views.pagar, name='pagar'),
    path('get-time/', views.get_time, name='get_time'),
    path('mangas/', mangas, name="mangas"),
    path('adminDelete/<id>/', adminDelete, name="adminDelete"),
    path('eliminar_todo_del_carrito/<int:producto_id>/', views.eliminar_todo_del_carrito, name='eliminar_todo_del_carrito'),
]