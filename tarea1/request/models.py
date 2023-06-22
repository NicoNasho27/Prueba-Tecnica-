# Archivo que define la estructura de la información que se va a almacenar en la Base de Datos
# Debido a que la cantidad de campos que se obtienen del objeto JSON es demasiado grande
# Escogí los campos que a mi parecer eran los más relevantes

from django.db import models
from django.contrib.postgres.fields import ArrayField

# Clase de Jurisprudencias, que gracias a Django esta se convierte directamente en una tabla dentro de la base de datos

class Jurisprudencias(models.Model):
    id = models.BigIntegerField(primary_key=True)
    tribunal = models.CharField(max_length=70)
    tipo_causa = models.CharField(max_length=15)
    tipo_recurso = models.CharField(max_length=100)
    rol = models.CharField(max_length=20)
    caratula = models.CharField(max_length=255)
    nombre_Proyecto = models.CharField(max_length=255)
    fecha_sentencia = models.DateField()
    descriptores = ArrayField(ArrayField(models.CharField(max_length=100)))
    decision_del_tribunal = models.CharField(max_length=255)
    competencia = models.CharField(max_length=255)
    ministro_redactor = models.CharField(max_length=40)