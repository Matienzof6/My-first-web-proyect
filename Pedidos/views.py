from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Pedidos.models import LineaPedido, Pedido
from Carro.carro import Carro
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from Tienda.models import Producto

# Create your views here.
@login_required(login_url="autenticacion/logear")
def procesar_pedido(request):
    pedido=Pedido.objects.create(user=request.user)
    carro=Carro(request)    
    lineas_pedido=list()

    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(
            producto_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido
        ))
    
    LineaPedido.objects.bulk_create(lineas_pedido)

    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombreUsuario=request.user.username,
        emailUsuario=request.user.email,
    )

    messages.success(request, "El pedido se ha creado correctamente")

    return redirect("../shop")

def enviar_mail(**kwargs):
    asunto="Gracias por su pedido"
    mensaje=render_to_string("emails/pedido.html",{
        "pedido": kwargs.get("pedido"),
        "lineas_pedido": kwargs.get("lineas_pedido"),
        "nombreUsuario": kwargs.get("nombreUsuario")
    })
    
    mensaje_texto=strip_tags(mensaje)
    from_email="contactobuces@gmail.com"
    to=kwargs.get("emailUsuario")

    send_mail(asunto,mensaje_texto,from_email,[to], html_message=mensaje)