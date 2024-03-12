from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),

    path('categorias/', categoria, name="categorias"),
    path('about/', About, name="about"),
    path('', inicio, name="inicio"),
    path('productos/<int:categoria_id>/', productos_por_categoria, name='productos_por_categoria'),
    path('productos/', productos, name='productos'),

    #formularios

    path('cliente_form/', clienteForm, name="clienteform"),
    path('producto_form/', productoForm, name="productoForm"),
    path('categoria_form/', categoriaForm, name="categoriaForm"),

    #Busquedas

    path('encontrar_producto/', encontrarProducto, name="encontrar_productos"),
]
