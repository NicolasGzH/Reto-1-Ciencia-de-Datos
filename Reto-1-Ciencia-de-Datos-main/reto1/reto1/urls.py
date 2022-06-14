import imp
from os import stat
from xml.dom.minidom import Document
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from reto1.Vista.views import Pagina_Inicio,Primera_Consulta,Primera_ConsultaR,Segunda_Consulta,Segunda_ConsultaR,Tercera_Consulta,Tercera_ConsultaR,Cuarta_Consulta,Cuarta_ConsultaR,Quinta_Consulta,Quinta_ConsultaR,Sexta_Consulta,Sexta_ConsultaR


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",Pagina_Inicio),     

    path("Consulta1/",Primera_Consulta),
    path("Consulta1/Consulta1R/",Primera_ConsultaR),

    path("Consulta2/",Segunda_Consulta),
    path("Consulta2/Consulta2R/",Segunda_ConsultaR),

    path("Consulta3/",Tercera_Consulta),
    path("Consulta3/Consulta3R/",Tercera_ConsultaR),

    path("Consulta4/",Cuarta_Consulta),
    path("Consulta4/Consulta4R/",Cuarta_ConsultaR),

    path("Consulta5/",Quinta_Consulta), 
    path("Consulta5/Consulta5R/",Quinta_ConsultaR),
    
    path("Consulta6/",Sexta_Consulta), 
    path("Consulta6/Consulta6R/",Sexta_ConsultaR),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
