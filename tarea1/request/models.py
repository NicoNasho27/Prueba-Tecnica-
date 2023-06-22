from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Jurisprudencias(models.Model):
    id = models.BigIntegerField(primary_key=True)
    tribunal = models.CharField(max_length=70)
    tipo_causa = models.CharField(max_length=15)
    tipo_recurso = models.CharField(max_length=100)
    rol = models.CharField(max_length=20)
    caratula = models.CharField(max_length=255)
    nombre_Proyecto = models.CharField(max_length=255)
    fecha_sentencia = models.DateField()
    descriptores = ArrayField(ArrayField(models.CharField(max_length=20)))
    decision_del_tribunal = models.CharField(max_length=255)
    competencia = models.CharField(max_length=255)
    ministro_redactor = models.CharField(max_length=40)