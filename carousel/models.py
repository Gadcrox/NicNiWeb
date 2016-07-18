from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Carousel(models.Model):
    class Meta():
        db_table = "carousel"

    titulo = models.CharField(max_length = 100, null = False)
    caption = models.CharField(max_length = 100, null = False)
    imagen = models.FileField(upload_to='carousel/', blank=True, null=True)
