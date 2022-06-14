from cgitb import html
from importlib.resources import path
import os
import pandas as pd
import numpy as np
from sodapy import Socrata
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template,Context,loader

def Cargar_Df():  #Función para cargar el DataFrame mediante el uso de sodapy y socrata
    client = Socrata("www.datos.gov.co", None)
    results = client.get("prrv-jnta", limit=1000)
    results_df = pd.DataFrame.from_records(results)
    return results_df  

def Pagina_Inicio(request):
    pd.set_option('colheader_justify', 'center')     
    doc_plantilla=loader.get_template("index.html")
    documento=doc_plantilla.render()
    return HttpResponse(documento)

def Primera_Consulta(request):

    consulta=Cargar_Df()
    doc_plantilla=loader.get_template("PrimeraConsulta.html")
    documento=doc_plantilla.render({"df":consulta.to_html()})

    return HttpResponse(documento)

def Primera_ConsultaR(request):
    filtro=request.GET.get('territorio')
    
    consulta=Cargar_Df()
   
    consulta=consulta[consulta['nom_territorio'] == filtro]
    doc_plantilla=loader.get_template("PrimeraConsultaR.html")
    documento=doc_plantilla.render({"df":consulta.to_html(), 'departamento':filtro})
    return HttpResponse(documento)    

def Segunda_Consulta(request):
    consulta=Cargar_Df()
    doc_plantilla=loader.get_template("SegundaConsulta.html")
    documento=doc_plantilla.render({"df":consulta.to_html()})
    return HttpResponse(documento)

def Segunda_ConsultaR(request):
    filtro=request.GET.get('codigo')
    consulta=Cargar_Df()
    consulta[['cod_territorio']]=consulta[['cod_territorio']].astype(int)
    consulta=consulta[consulta['cod_territorio'] >= int(filtro)]
    consulta=consulta.sort_values('cod_territorio')
    doc_plantilla=loader.get_template("SegundaConsultaR.html")
    documento=doc_plantilla.render({"df":consulta.to_html(), 'cod':filtro})

    return HttpResponse(documento)       

def Tercera_Consulta(request):

    consulta=Cargar_Df()
    doc_plantilla=loader.get_template("TerceraConsulta.html")
    documento=doc_plantilla.render({"df":consulta.to_html()})

    return HttpResponse(documento)   

def Tercera_ConsultaR(request):
    filtro=request.GET.get('dosis')
    consulta=Cargar_Df()
    consulta[['cantidad_dosis_aplicadas']]=consulta[['cantidad_dosis_aplicadas']].astype(int)
    consulta=consulta[consulta['cantidad_dosis_aplicadas'] >= int(filtro)]
    consulta=consulta.sort_values('cantidad_dosis_aplicadas')
    doc_plantilla=loader.get_template("TerceraConsultaR.html")
    documento=doc_plantilla.render({"df":consulta.to_html(), 'dosis':filtro})

    return HttpResponse(documento) 


def Cuarta_Consulta(request):

    consulta=Cargar_Df()
    doc_plantilla=loader.get_template("CuartaConsulta.html")
    documento=doc_plantilla.render({"df":consulta.to_html()})

    return HttpResponse(documento)

def Cuarta_ConsultaR(request):
    filtro=request.GET.get('año')
    consulta=Cargar_Df()
    consulta[['a_o']]=consulta[['a_o']].astype(int)
    consulta=consulta[consulta['a_o'] == int(filtro)]
    doc_plantilla=loader.get_template("CuartaConsultaR.html")
    documento=doc_plantilla.render({"df":consulta.to_html(), 'año':filtro})

    return HttpResponse(documento)     

def Quinta_Consulta(request):

    consulta=Cargar_Df()
    doc_plantilla=loader.get_template("QuintaConsulta.html")
    documento=doc_plantilla.render({"df":consulta.to_html()})

    return HttpResponse(documento)     

def Quinta_ConsultaR(request):
    filtro1=request.GET.get('filtro1')
    filtro2=request.GET.get('filtro2')
    consulta=Cargar_Df()
    consulta[['cantidad_dosis_aplicadas']]=consulta[['cantidad_dosis_aplicadas']].astype(int)
    consulta=consulta[(consulta['cantidad_dosis_aplicadas'] >= int(filtro2)) &(consulta['nom_territorio'] == filtro1)]
    doc_plantilla=loader.get_template("QuintaConsultaR.html")
    documento=doc_plantilla.render({"df":consulta.to_html(), 'territorio':filtro1, 'dosisa':filtro2})

    return HttpResponse(documento)

def Sexta_Consulta(request):

    consulta=Cargar_Df()
    doc_plantilla=loader.get_template("SextaConsulta.html")
    documento=doc_plantilla.render({"df":consulta.to_html()})

    return HttpResponse(documento)     

def Sexta_ConsultaR(request):
    
    filtro=request.GET.get('ID')
    consulta=Cargar_Df()
    consulta=consulta.loc[[int(filtro)]]
    doc_plantilla=loader.get_template("SextaConsultaR.html")
    documento=doc_plantilla.render({"df":consulta.to_html(), 'ID':filtro})

    return HttpResponse(documento)        
