from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProveedorViewSet, ProductoViewSet, ClienteViewSet, VentaViewSet, VentaDetalleViewSet, CategoriaViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'proveedores', ProveedorViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'ventas', VentaViewSet)
router.register(r'venta-detalles', VentaDetalleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
