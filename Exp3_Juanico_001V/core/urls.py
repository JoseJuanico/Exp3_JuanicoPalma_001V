from django.urls import path
from .views import index, clases, confirmacion, horarioAtencion, plan, quienSomos, registro, basededatos, crearUsuario 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path ('', index, name = "index"), #con este metodo se llama a la pagina index como primer opcion para mirar
    path ('clases/', clases, name = "clases"),
    path ('confirmacion/', confirmacion, name = "confirmacion"),
    path ('horarioAtencion/', horarioAtencion, name = "horarioAtencion"),
    path ('plan/', plan, name = "plan"),
    path ('quienSomos/', quienSomos, name = "quienSomos"),
    path ('registro/', registro, name = "registro"),
    path ('core/basededatos/', basededatos, name = "basededatos"),
    path ('crearUsuario', crearUsuario, name = "crearUsuario")
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)