from tkinter import Label
from django import forms

class FormularioContacto(forms.Form):

    nombre=forms.CharField(label="Nombre", required=True, max_length=40)
    email=forms.EmailField(label="Email", required=True, max_length=40)
    contenido=forms.CharField(label="Mensaje", max_length=200, widget=forms.Textarea)

    