from django.shortcuts import render
from .models import Tipo, Usuario

# Create your views here.

def index (request):
    usuario = Usuario.objects.all() #acceso a los usuarios ya creados por admin
    return render (request, 'index.html', context = {'datos': usuario})

def clases (request):
    return render (request, 'clases.html')

def confirmacion (request):
    return render (request, 'confirmacion.html')

def horarioAtencion (request):
    return render (request, 'horarioAtencion.html')

def plan (request):
    return render (request, 'plan.html')

def quienSomos (request):
    return render (request, 'quienSomos.html')

def registro (request):
    return render (request, 'registro.html')