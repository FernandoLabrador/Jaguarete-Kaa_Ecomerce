from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Categoria(models.Model):
    descripcion = models.CharField(max_length=64, null=False)

    def __str__(self):
        return f"{self.descripcion}"


class Producto(models.Model):
    titulo = models.CharField(max_length=250, null=False)
    imagen = models.ImageField(upload_to='imagenes/')
    descripcion_producto = models.CharField(max_length=2000, null=False)
    precio = models.FloatField()
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, related_name="categoria_producto")

    def __str__(self):
        return f"{self.categoria} - {self.titulo} ({self.precio})"


class Carrito(models.Model):
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="usuario")
    lista_productos = models.ManyToManyField(
        Producto, blank=True, null=True, related_name="carrito")
    total_carrito = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.usuario} - {self.lista_productos}"
