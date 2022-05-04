from django.db import models

# Create your models here.

class Menu(models.Model):
    imagen = models.CharField(max_length=500)


