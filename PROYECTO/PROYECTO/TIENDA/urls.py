from django.urls import path
from django.urls import path
from . import views

app_name = "TIENDA"
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:producto_id>', views.producto, name="producto"),
    path('producto_alta/', views.producto_alta, name="producto_alta"),
    path('producto_editar/<int:producto_id>',
         views.producto_editar, name="producto_editar"),
    path('producto_eliminar/<int:producto_id>',
         views.producto_eliminar, name="producto_eliminar"),
    path('carrito/<int:producto_id>', views.carrito, name="carrito"),
    path('carrito/', views.carrito, name="carrito"),
    path('carrito_eliminar/<int:producto_id>',
         views.carrito_eliminar, name="carrito_eliminar"),
    path('carrito_eliminar/', views.carrito_eliminar, name="carrito_eliminar"),
    path('busqueda/<int:categoria_id>', views.buscador, name="buscador"),
    path('busqueda/', views.buscador, name="buscador"),
    path('acerca_de/', views.acerca_de, name="acerca_de"),
]
