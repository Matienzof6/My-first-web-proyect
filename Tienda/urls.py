from django.urls import path
from Tienda import views




urlpatterns = [
    path('', views.shop, name='Shop'),
]