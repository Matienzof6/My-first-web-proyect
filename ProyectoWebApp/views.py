from django.shortcuts import render
from django.http import HttpResponse
from Carro.carro import Carro
from Servicios.models import Servicio

def home(request):

    carro=Carro(request)

    return render(request,'ProyectoWebApp/home.html')





