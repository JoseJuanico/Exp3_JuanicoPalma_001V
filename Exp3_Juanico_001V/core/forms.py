from django import forms
from django.db.models.base import Model
from django.forms import ModelForm, widgets
from .models import Usuario

class UsuarioForm(ModelForm): 
	class Meta:
		model = Usuario #clase con la que se vincula el formulario
		fields = ['rut', 'nombre', 'apellido', 'correo', 'contrasena', 'tipo']

		labels = { #se le da palabras a los labels segun el atributo del models
			'rut': 'Ingrese el rut',  #rut se refiere al atributo y lo siguiente es lo que dira el label en la pagina
			'nombre': 'Ingrese el nombre',
			'apellido': 'Ingrese el apellido',
			'correo': 'Ingrese el correo electrónico',
			'contrasena': 'Ingrese la contrasena',
			'tipo': 'Ingrese el tipo de usuario',
		}

		widgets = { #permite definir que tipo de elementos se insertan en el html para ingresar informacion
			'rut': forms.TextInput(
				attrs = {
					'class': 'form-control',
					'placeholder': 'Ingrese rut sin puntos...',
					'id': 'lrut',
					'name': 'lrut',
				}
			),
			'nombre': forms.TextInput(
				attrs = {
					'class': 'form-control',
					'placeholder': 'Ingrese nombres...',
					'id': 'lnombre',
					'name': 'lnombre',
				}
			),
			'apellido': forms.TextInput(
				attrs = {
					'class': 'form-control',
					'placeholder': 'Ingrese apellidos...',
					'id': 'lapellido',
					'name': 'lapellido',
				}
			),
			'correo': forms.EmailInput(
				attrs = {
					'class': 'form-control',
					'placeholder': 'Ingrese correo electrónico...',
					'id': 'lcorreo',
					'name': 'lcorreo',
				}
			),
			'contrasena': forms.TextInput(
				attrs = {
					'class': 'form-control',
					'placeholder': 'Ingrese contraseña...',
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
