from django.db import models

# Create your models here.
#Aca deberia actualizar por las clases de productos que quiero vender en mi pagina de indumentaria.

class Categoria(models.Model):#podria ser ropa urbana/deporte
    nombre  = models.CharField(max_length=40)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):#Segun la categoria, tengo cierto producto.
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre  = models.CharField(max_length=120)
    precio  = models.DecimalField(max_digits=10, decimal_places=2)
    imagen_url = models.URLField(default='https://dummyimage.com/450x300/dee2e6/6c757d.jpg')  

    def __str__(self):
        return self.nombre
    
class Cliente(models.Model):#base de datos de los clientes que compran.
    nombre  = models.CharField(max_length=40)
    apellido  = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre}+{self.apellido}, email = {self.email}"

class Carrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)  
    cantidad = models.IntegerField(default=1)  
