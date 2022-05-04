from django.db import models

# Create your models here.

class Encuesta(models.Model):
    nombre = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    fecha_nac = models.DateField()
