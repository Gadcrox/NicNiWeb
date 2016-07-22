from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Configuration(models.Model):
    class Meta():
        db_table = "configuration"

    historia = models.TextField(null = True)
    concepto = models.TextField(null = True)
    telefono = models.CharField(max_length = 30, null = True)
    correo = models.EmailField(null = True)
    direccion = models.CharField(max_length = 1000, null = True)
    codigo_postal = models.CharField(max_length = 6, null = True)
    facebook = models.CharField(max_length = 100, null = True)
    google_plus = models.CharField(max_length = 100, null = True)
    linkedin = models.CharField(max_length = 100, null = True)
    instagram = models.CharField(max_length = 100, null = True)
    twitter = models.CharField(max_length = 100, null = True)
