from django.contrib import admin
from .models import Proveedor, Producto, Cliente, Venta, VentaDetalle, Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cantidad', 'precio', 'costo', 'proveedor', 'categoria', 'imagen_url')
    search_fields = ('nombre', 'proveedor__nombre', 'categoria__nombre')
    list_filter = ('proveedor', 'categoria')
    fields = ('nombre', 'cantidad', 'precio', 'costo', 'proveedor', 'categoria', 'imagen_url')
    list_editable = ('cantidad', 'precio', 'costo', 'imagen_url')

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'contacto')
    search_fields = ('nombre',)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'direccion')
    search_fields = ('nombre', 'email')

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'fecha', 'total')
    search_fields = ('cliente__nombre',)
    list_filter = ('fecha',)
    readonly_fields = ('total',)

@admin.register(VentaDetalle)
class VentaDetalleAdmin(admin.ModelAdmin):
    list_display = ('venta', 'producto', 'cantidad', 'precio')
    search_fields = ('producto__nombre', 'venta__cliente__nombre')
    list_filter = ('producto',)
