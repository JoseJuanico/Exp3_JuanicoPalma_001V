from django.urls import path
from .views import index, clases, confirmacion, horarioAtencion, plan, quienSomos, registro 

urlpatterns = [
    path ('', index, name = "index"), #con este metodo se llama a la pagina index como primer opcion para mirar
    path ('clases/', clases, name = "clases"),
    path ('confirmacion/', confirmacion, name = "confirmacion"),
    path ('horarioAtencion/', horarioAtencion, name = "horarioAtencion"),
    path ('plan/', plan, name = "plan"),
    path ('quienSomos/', quienSomos, name = "quienSomos"),
    path ('registro/', registro, name = "registro"),
]