from django import forms
from django.db.models.base import Model
from django.forms import ModelForm
from .models import Usuario, Vehiculo

class UsuarioForm(ModelForm): 
	class Meta:
		model = Usuario
		fields = ['rut', 'nombre', 'apellido', 'correo', 'contrasena', 'tipo']
