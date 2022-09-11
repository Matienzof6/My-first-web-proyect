from django.shortcuts import render
from Servicios.models import Servicio
# Create your views here.



def services(request):

    servicios=Servicio.objects.all()
    return render(request,'Servicios/services.html', {'servicios':servicios})
