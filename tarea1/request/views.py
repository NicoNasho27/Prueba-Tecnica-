# Archivo de vistas de este módulo
# Este archivo se encarga de obtener la lista de jurisprudencias y subirlas a la base de datos
# 

from django.shortcuts import render
import requests
from django.http import HttpResponse
from .models import Jurisprudencias
import datetime

# Función que obtiene la lista de jurisprudencias de la página

def post(request):

    # Este es un objeto JSON que define los parámetros de la busqueda, el atributo "search" se encuentra vacío ya que se quieren obtener todas
    # Las jurisprudencias que existen
    # Para este caso solo se están obteniendo 10, pero de querer obtenerlas todas, se debería cambiar el atributo "pageSize" a 757
    # Que es la cantidad actual de jurisprudencias que existen
    search = {"page": "1","pageSize": "10" ,"search": "", "orden": "nuevo"}
    #Se hace la petición post a API de la página utilizando el objeto anterior y se almacena en una variable
    data = requests.post('https://www.buscadorambiental.cl/buscador-api/jurisprudencias/list',json=search)

    # Debido a que la respuesta tiene mucha información, esta se convierte a formato JSON y se almacena en una variable
    # Unicamente la información referida a las jurisprudencias
    datos = data.json()['jurisprudencias']
    
    # Ciclo iterativo que recorre todas las jurisprudencias que se obtuvieron y las envía a la función "upload" para cargarlas a la Base de Datos
    for i in range(len(data.json()['jurisprudencias'])):
        upload(data.json()['jurisprudencias'][i])
    
    # Aquí se envían los datos para ser vistos mediante el navegador
    return HttpResponse([datos])


# Función que Carga cada jurisprudencia que recibe a la Base de Datos
def upload(data):

    # Primero se convierte la fecha de la sentencia de tipo String o cadena de carácteres a un objeto de tipo fecha
    date = datetime.datetime.strptime(data['fechaSentencia'],"%d-%m-%Y")
    # Luego la fecha se convierte a otro formato, ya que Postgres por defecto maneja fechas del tipo "YYYY-MM-DD"
    f_date = datetime.datetime.strftime(date,"%Y-%m-%d")
    # Se obtienen los descriptores de la jurisprudencia
    d = data['descriptores']
    # Estos se separan, ya que estan todos en un solo objeto de tipo String y en el modelo esto se definio como un atributo de tipo Arreglo
    d_split = d.split(";")
    # Analizando la estructura de la información obtenida, me di cuenta de que para cada jurisprudencia la información estaba en diferentes 
    # posiciones
    # Es por esto que para cada uno de estos datos, realizo una busqueda dentro del objeto JSON, para determinar con la mayor precisión posible
    # La posición de la información que se necesita
    lista1 = (list(filter(lambda x:x["parametro"]=="MINISTRO REDACTOR TA", data['valores'])))
    lista2 = (list(filter(lambda x:x["parametro"]=="DECISIÓN DEL TRIBUNAL", data['valores'])))
    lista3 = (list(filter(lambda x:x["parametro"]=="COMPETENCIA", data['valores'])))
    # Strings vacíos, ya que en algunos casos estos no están presentes en el objeto JSON y otras si
    causa = ''
    recurso = ''
    # Se utiliza la función Try, para evitar errores en tiempo de ejecución 
    try:
        # Se utiliza varios condicionales a fin de que la información que se guarde en la Base de datos sea mas descriptiva
        # Ya que por defecto en el objeto JSON, este dato en particular solo es representado con un solo caracter
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
    
    # Misma operación para el tipo de recurso, la diferencia radica en que este puede no estar presente dentro del objeto
    try:
       lista4 = (list(filter(lambda x:x["parametro"]=="TIPO DE RECURSO", data['valores'])))
       recurso = lista4[0]['item'] 
    except:
        recurso='N/A'     
    
    # Similar al caso del tipo de Causa, la información dentro del objeto no es muy descriptiva
    tribunal = ''
    # En este caso, se utiliza el try para verificar si hay más de un tribunal involucrado, en cuyo caso este quedará como el 
    # Que se está mostrando en la página
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

    
    # Se crea un objeto de Tipo Jurisprudencias, el cual es una instancia de la clase creada en el archivo "models.py"
    # Este objeto recibe todos los datos que se obtuvieron anteriormente
    j = Jurisprudencias(id=data['id'],tribunal = tribunal,tipo_causa=causa,tipo_recurso=recurso, rol=data['rol'], caratula= data['caratula'], nombre_Proyecto=data['nombreProyecto'],fecha_sentencia = f_date, descriptores = d_split, decision_del_tribunal = lista2[0]['item'], competencia = lista3[0]['item'], ministro_redactor=lista1[0]['item'])
    # Función que guarda el objeto creado en la Base de Datos 
    j.save()