from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify


class Tags(models.Model):
    class Meta():
        db_table = "tags"
    name = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Tags, self).save(*args, **kwargs)

class Article(models.Model):
    class Meta():
        db_table = "article"
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True)
    body = models.TextField()
    author = models.CharField(max_length = 100)
    tags = models.ManyToManyField(Tags, related_name="article_tags")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    imagen = models.FileField(upload_to='news/', blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Article, self).save(*args, **kwargs)

    def get_string_tags(self):
        return ', '.join([tags.name for tags in self.tags.all()])
