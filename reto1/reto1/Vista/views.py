from django.http import HttpResponse
import pandas as pd
from sodapy import Socrata
from django.shortcuts import render
from django.template import Template,Context,loader

def Cargar_Df():  #Función para cargar el DataFrame mediante el uso de sodapy y socrata
    client = Socrata("www.datos.gov.co", None)
    results = client.get("prrv-jnta", limit=1000)
    results_df = pd.DataFrame.from_records(results)

    return results_df  

def Pagina_Inicio(request):

    DataFrame=Cargar_Df()
    doc_plantilla=loader.get_template("PaginaInicio.html")
    documento=doc_plantilla.render({"df":DataFrame.to_html()})

    return HttpResponse(documento)        

def Primera_Consulta(request):

    consulta=Cargar_Df()
    #consulta=consulta.isnull() 

    doc_plantilla=loader.get_template("PrimeraConsulta.html")
    documento=doc_plantilla.render({"df":consulta.to_html()})

    return HttpResponse(documento)

def Segunda_Consulta(request):

    consulta=Cargar_Df()
    #consulta=consulta.isnull() 

    doc_plantilla=loader.get_template("SegundaConsulta.html")
    documento=doc_plantilla.render({"df":consulta.to_html()})

    return HttpResponse(documento)

def Tercera_Consulta(request):

    consulta=Cargar_Df()
    #consulta=consulta.isnull() 

    doc_plantilla=loader.get_template("TerceraConsulta.html")
    documento=doc_plantilla.render({"df":consulta.to_html()})

    return HttpResponse(documento)   

def Cuarta_Consulta(request):

    consulta=Cargar_Df()
    #consulta=consulta.isnull() 

    doc_plantilla=loader.get_template("CuartaConsulta.html")
    documento=doc_plantilla.render({"df":consulta.to_html()})

    return HttpResponse(documento)

def Quinta_Consulta(request):

    consulta=Cargar_Df()
    #consulta=consulta.isnull() 

    doc_plantilla=loader.get_template("QuintaConsulta.html")
    documento=doc_plantilla.render({"df":consulta.to_html()})

    return HttpResponse(documento)         