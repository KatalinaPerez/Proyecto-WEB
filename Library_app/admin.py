from django.contrib import admin
from .models import Libro


#modelo para visualizacion tabla en admin
class LibroAdmin(admin.ModelAdmin):
    list_display = ["titulo", "autor", "precio"]
    list_editable =["precio"]
    search_fields= ["titulo", "autor"]

# Register your models here.
admin.site.register(Libro, LibroAdmin)
#admin.site.register(Carrito)


