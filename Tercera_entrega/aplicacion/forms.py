from django import forms
from .models import *

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()


class ProductoForm(forms.Form):
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all())
    nombre = forms.CharField(max_length=120)
    precio = forms.DecimalField(max_digits=10, decimal_places=2)
    imagen_url = forms.URLField()

class CategoriaForm(forms.Form):
    nombre = forms.CharField(max_length=40)

    