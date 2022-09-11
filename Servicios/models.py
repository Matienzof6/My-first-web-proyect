from django.db import models

# Create your models here.

class Servicio(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=250)
    imagen=models.ImageField(upload_to='Servicios')
    created=models.DateTimeField(auto_now_add=True) #Para agregar la fecha automaticamente auto_now_add
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Servicio'
        verbose_name_plural='Servicios'

    def __str__(self):
        
        return self.titulo