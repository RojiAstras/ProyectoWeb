from django.contrib import admin
from .models import Producto, Boleta, DetalleBoleta, Empleado, Cliente, Carusel1, Carusel2, Banner, Carrito, TipoArticulo, TipoMascota

# Register your models here.
admin.site.register(TipoArticulo)
admin.site.register(TipoMascota)
admin.site.register(Producto)
admin.site.register(Carrito)
admin.site.register(Boleta)
admin.site.register(DetalleBoleta)
admin.site.register(Empleado)
admin.site.register(Cliente)
admin.site.register(Carusel1)
admin.site.register(Carusel2)
admin.site.register(Banner)
