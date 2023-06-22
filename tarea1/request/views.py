from django.shortcuts import render
import requests
from django.http import HttpResponse
from .models import Jurisprudencias
import datetime

# Create your views here.

def post(request):

    search = {"page": "1","pageSize": "10" ,"search": "", "orden": "nuevo"}
    data = requests.post('https://www.buscadorambiental.cl/buscador-api/jurisprudencias/list',json=search)

    datos = data.json()['jurisprudencias']
    
    for i in range(len(data.json()['jurisprudencias'])):
        upload(data.json()['jurisprudencias'][i])
    
    return HttpResponse([datos])



def upload(data):

    date = datetime.datetime.strptime(data['fechaSentencia'],"%d-%m-%Y")
    f_date = datetime.datetime.strftime(date,"%Y-%m-%d")
    d = data['descriptores']
    d_split = d.split(";")
    lista1 = (list(filter(lambda x:x["parametro"]=="MINISTRO REDACTOR TA", data['valores'])))
    lista2 = (list(filter(lambda x:x["parametro"]=="DECISIÓN DEL TRIBUNAL", data['valores'])))
    lista3 = (list(filter(lambda x:x["parametro"]=="COMPETENCIA", data['valores'])))
    causa = ''
    recurso = ''
    try:
        c = data['tipoCausa']
        causa = ''
        if c == "S":
            causa =  "Solicitud"

        elif (c=="R"): 
                causa = "Reclamacion"
        elif (c=="D"):
                causa = "Demanda"
        elif (c=="C"):
            causa = "Consulta"
    except:
        causa = "N/A"
    
    try:
       lista4 = (list(filter(lambda x:x["parametro"]=="TIPO DE RECURSO", data['valores'])))
       recurso = lista4[0]['item'] 
    except:
        recurso='N/A'     
    
    tribunal = ''

    try:
        lista5 = (list(filter(lambda x:x["parametro"]=="TRIBUNAL CS/CA", data['valores'])))
        tribunal = lista5[0]["item"]
    except:
        if(data["tribunal"] == "1TA" ):
            tribunal = "Primer Tribunal Ambiental"
        elif (data["tribunal"] == "2TA"):
            tribunal = "Segundo Tribunal Ambiental"
        elif (data["tribunal"] == "3TA"):
            tribunal = "Tercer Tribunal Ambiental"

    

    j = Jurisprudencias(id=data['id'],tribunal = tribunal,tipo_causa=causa,tipo_recurso=recurso, rol=data['rol'], caratula= data['caratula'], nombre_Proyecto=data['nombreProyecto'],fecha_sentencia = f_date, descriptores = d_split, decision_del_tribunal = lista2[0]['item'], competencia = lista3[0]['item'], ministro_redactor=lista1[0]['item']) 
    j.save()