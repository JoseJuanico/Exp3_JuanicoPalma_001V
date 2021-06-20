from django import forms
from django.db.models.base import Model
from django.forms import ModelForm, widgets
from .models import Usuario

class UsuarioForm(ModelForm): 
	class Meta:
		model = Usuario 
		fields = ['rut', 'nombre', 'apellido', 'correo', 'contrasena', 'tipo']

		labels = { 
			'rut': 'Ingrese el rut (EJ.10637553-2)',  
			'nombre': 'Ingrese el nombre',
			'apellido': 'Ingrese el apellido',
			'correo': 'Ingrese el correo electrónico',
			'contrasena': 'Ingrese la contraseña',
			'tipo': 'Ingrese el tipo de usuario',
			'editar': 'Editar',
			'eliminar': 'Borrar de base de datos',
		}

		widgets = {
			'rut': forms.TextInput(
				attrs = {
					'class': 'form-control',
					'placeholder': 'Rut sin puntos...',
					'id': 'lrut',
					'name': 'lrut',
				}
			),
			'nombre': forms.TextInput(
				attrs = {
					'class': 'form-control',
					'placeholder': 'Nombres...',
					'id': 'lnombre',
					'name': 'lnombre',
				}
			),
			'apellido': forms.TextInput(
				attrs = {
					'class': 'form-control',
					'placeholder': 'Apellidos...',
					'id': 'lapellido',
					'name': 'lapellido',
				}
			),
			'correo': forms.EmailInput(
				attrs = {
					'class': 'form-control',
					'placeholder': 'Correo electrónico...',
					'id': 'lcorreo',
					'name': 'lcorreo',
				}
			),
			'contrasena': forms.PasswordInput(
				attrs = {
					'class': 'form-control',
					'placeholder': 'Máx. 9 caracteres...',
					'id': 'lpassword1',
					'name': 'lpassword1',
				}
			),
			'tipo': forms.Select(
				attrs = {
					'class': 'form-control',
					'id': 'tipo',
				}
			)
		}
