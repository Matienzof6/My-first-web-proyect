from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage
# Create your views here.


def contact(request):
    formulario_contacto=FormularioContacto()

    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            mensaje=request.POST.get("contenido")
            
            
            email=EmailMessage('Mensaje desde app Django',"El usuario con nombre {} y direccion {} escribe: \n\n {}".format(nombre,email,mensaje),'',['matienzof6@gmail.com'],reply_to=[email])

            try:
                email.send()
            
                return redirect("/contact/?valido")
            except:

                return redirect("/contact/?novalido")



    return render(request,'contacto/contact.html', {'miFormulario':formulario_contacto})
