from django.contrib import admin
from django.urls import path
from reto1.Vista.views import Pagina_Inicio,Primera_Consulta,Segunda_Consulta,Tercera_Consulta,Cuarta_Consulta,Quinta_Consulta

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",Pagina_Inicio),
    path("Consulta1/",Primera_Consulta),
    path("Consulta2/",Segunda_Consulta),
    path("Consulta3/",Tercera_Consulta),
    path("Consulta4/",Cuarta_Consulta),
    path("Consulta5/",Quinta_Consulta),
]
