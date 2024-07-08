from django.contrib import admin
from .models import Producto, TipoLibro, Carrito

#modelo para visualizacion tabla en admin
class ProductoAdmin(admin.ModelAdmin):
    list_display = ["titulo", "autor", "precio", "categoria", "tipolibro"]
    list_editable = ["precio"]
    search_fields = ["nombre", "autor"]
    list_filter = ["tipolibro", "autor", "categoria"]
    list_per_page = 10

#visualizacion de carrito
class CarritoAdmin(admin.ModelAdmin):
    list_display = ["producto", "cantidad", "agregado_en"]


# Register your models here.
admin.site.register(TipoLibro)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Carrito)
#admin.site.register(Carrito)

