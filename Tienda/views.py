from django.shortcuts import render

from .models import Producto

# Create your views here.

def shop(request):
    productos=Producto.objects.all()
    return render(request,'Tienda/shop.html', {'productos':productos})

