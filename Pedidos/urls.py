from django.urls import path
from Pedidos import views




urlpatterns = [
    path('', views.procesar_pedido, name='procesar_pedido'),
]