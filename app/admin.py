from django.contrib import admin
from .models import TipoLibro, Producto
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["titulo", "autor", "precio", "categoria", "tipolibro"]
    list_editable = ["precio"]
    search_fields = ["nombre", "autor"]
    list_filter = ["tipolibro", "autor", "categoria"]
    list_per_page = 10

admin.site.register(TipoLibro)
admin.site.register(Producto, ProductoAdmin)
