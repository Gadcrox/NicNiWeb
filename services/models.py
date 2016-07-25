from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify
# Create your models here.

class Services(models.Model):
    class Meta():
        db_table = "services"

    titulo = models.CharField(max_length = 100, null = False)
    slug = models.CharField(max_length = 100, null = False, unique = True)
    descripcion = models.TextField(null = False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        return super(Services, self).save(*args, **kwargs)
