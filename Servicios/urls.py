from django.urls import path
from Servicios import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('', views.services, name='Services'),
]

