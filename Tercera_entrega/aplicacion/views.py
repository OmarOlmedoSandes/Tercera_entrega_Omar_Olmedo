from django.shortcuts import render, redirect
from .models import *
from .forms import *

def home(request):
    categorias = Categoria.objects.all()  
    return render(request,"aplicacion/index.html",{"categorias":categorias})

def inicio(request):
    categorias = Categoria.objects.all()  
    return render(request,"aplicacion/inicio.html",{"categorias":categorias})

def categoria(request):
    categorias=Categoria.objects.all()
    return render(request, "aplicacion/categoria.html",{"categorias":categorias})

def productos(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    return render(request, 'aplicacion/productos.html', {'categorias': categorias, 'productos': productos})


def About(request):
    categorias=Categoria.objects.all()
    return render(request, "aplicacion/about.html",{"categorias":categorias})


def productos_por_categoria(request, categoria_id):
    try:
        categoria = Categoria.objects.get(pk=categoria_id)
        productos = Producto.objects.filter(categoria=categoria)
    except Categoria.DoesNotExist:
        # si no existe la categoria
        mensaje_error = "La categoría especificada no existe."
        return render(request, 'aplicacion/error.html', {'mensaje_error': mensaje_error})
    categorias = Categoria.objects.all()
    return render(request, 'aplicacion/productos_por_categoria.html', {'categoria': categoria, 'productos': productos,"categorias": categorias})

#-----------------------------------------------------------forms

def clienteForm(request):
    if request.method == "POST":
        #2 o n veces q ingresa
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            cliente_nombre = miForm.cleaned_data.get("nombre")
            cliente_apellido = miForm.cleaned_data.get("apellido")
            cliente_email = miForm.cleaned_data.get("email")
            cliente = Cliente(nombre=cliente_nombre, apellido=cliente_apellido, email=cliente_email)
            cliente.save()
            return render(request, "aplicacion/index.html")
        #sin el else se devuelve todos los errores con el else del if principal
    else :
        miForm = ClienteForm()
    return render(request,"aplicacion/clienteForm.html",{"form": miForm})

def productoForm(request):
    if request.method == "POST":
        #2 o n veces q ingresa
        miForm = ProductoForm(request.POST)
        if miForm.is_valid():
            producto_nombre = miForm.cleaned_data.get("nombre")
            producto_precio = miForm.cleaned_data.get("precio")
            producto_categoria = miForm.cleaned_data.get("categoria")
            producto_imagen = miForm.cleaned_data.get("imagen_url")
            producto = Producto(nombre=producto_nombre, precio=producto_precio, categoria=producto_categoria, imagen_url=producto_imagen)
            producto.save()
            categorias=Categoria.objects.all()
            return render(request, "aplicacion/index.html",{"categorias":categorias})
        #sin el else se devuelve todos los errores con el else del if principal
    else :
        miForm = ProductoForm()
    return render(request,"aplicacion/productoForm.html",{"form": miForm})

def categoriaForm(request):
    if request.method == "POST":
        #2 o n veces q ingresa
        miForm = CategoriaForm(request.POST)
        if miForm.is_valid():
            categoria_nombre = miForm.cleaned_data.get("nombre")
            categoria = Categoria(nombre=categoria_nombre)
            categoria.save()
            categorias=Categoria.objects.all()
            return render(request, "aplicacion/index.html",{"categorias":categorias})
        #sin el else se devuelve todos los errores con el else del if principal
    else :
         miForm = CategoriaForm()
    return render(request,"aplicacion/categoriaForm.html",{"form": miForm})


#para encontrar el producto
def encontrarProducto(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        productos=Producto.objects.filter(nombre__icontains=patron)
        categorias = Categoria.objects.all()
        contexto= {"productos":productos,"categorias": categorias}
        return render(request, "aplicacion/productos.html",contexto)
    
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    return render(request, 'aplicacion/productos.html', {'categorias': categorias, 'productos': productos})



