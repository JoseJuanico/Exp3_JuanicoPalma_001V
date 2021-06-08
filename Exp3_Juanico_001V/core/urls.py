from django.urls import path
from .views import index, clases, confirmacion, horarioAtencion, plan, quienSomos, registro 

urlpatterns = [
    path ('', index, name = "index"), #con este metodo se llama a la pagina index como primer opcion para mirar
    path ('', clases, name = "clases"),
    path ('', confirmacion, name = "confirmacion"),
    path ('', horarioAtencion, name = "horarioAtencion"),
    path ('', plan, name = "plan"),
    path ('', quienSomos, name = "quienSomos"),
    path ('', registro, name = "registro"),
]