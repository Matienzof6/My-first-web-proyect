from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class CategoriaProducto(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True) #Para agregar la fecha automaticamente auto_now_add
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Categoria Producto'
        verbose_name_plural='Categorias Productos'

    def __str__(self):
        
        return self.nombre



class Producto(models.Model):
    titulo=models.CharField(max_length=50)
    precio=models.FloatField()
    descripcion=models.CharField(max_length=250)
    imagen=models.ImageField(upload_to='Tienda', null=True, blank=True)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    categorias=models.ManyToManyField(CategoriaProducto)
    stock=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True) #Para agregar la fecha automaticamente auto_now_add
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Producto'
        verbose_name_plural='Productos'

    def __str__(self):
        
        return self.titulo