# -*- coding: utf-8 -*-
# encoding=utf8
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponse
import json, traceback
from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.conf import settings
from .models import Article, Tags

# Create your views here.
@login_required
def news_add_view(request):
    return render(request, 'addNews.html')

def news_modify_view(request):
    news_list = Article.objects.all().order_by('title')
    context = {'news_list': news_list}
    return render(request, 'modifyNews.html', context)

class create_news(TemplateView):
    def post(self, request, *args, **kwargs):
        if request.is_ajax() and request.method == 'POST':
            try:
                autor = request.POST.get('autor')
                titulo = request.POST.get('titulo')
                tags = request.POST.get('tags')
                contenido = request.POST.get('contenido')
                imagen = request.FILES.get('file', False)
            except:
                message = {'status':'1','message': str(traceback.format_exc())}
                data = json.dumps(message)
                return HttpResponse(data, content_type =  "application/json")

            try:
                if Article.objects.filter(title = titulo):
                    message = {'status':'2','message': 'Lo sentimos, este titulo ya ha siso registrado, por favor seleccione otro...'}
                    data = json.dumps(message)
                    return HttpResponse(data, content_type =  "application/json")
            except:
                message = {'status':'1','message': str(traceback.format_exc())}
                data = json.dumps(message)
                return HttpResponse(data, content_type =  "application/json")

            try:
                article_model = Article()
                article_model.title = titulo
                article_model.author = autor
                article_model.body = contenido
                article_model.imagen = imagen
                article_model.created_at = timezone.now()
                article_model.update_at = timezone.now()
                article_model.save()

                tags = tags.split(',')
                for tag in tags:
                    try:
                        tag_model = Tags.objects.get(name=tag.strip().upper())
                        article_model.tags.add(tag_model)
                        article_model.save()
                    except Tags.DoesNotExist:
                        tags_model = Tags()
                        tags_model.name = tag.strip().upper()
                        tags_model.save()
                        article_model.tags.add(tags_model)
                        article_model.save()

                message = {'status':'3','message': 'Datos ingresados satisfactoriamente.'}
                data = json.dumps(message)
                return HttpResponse(data, content_type =  "application/json")
            except:
                message = {'status':'1','message': str(traceback.format_exc())}
                data = json.dumps(message)
                return HttpResponse(data, content_type =  "application/json")

class view_new(TemplateView):
    def post(self, request, *args, **kwargs):
        if request.is_ajax() and request.method == 'POST':
            try:
                idNew = request.POST.get('idNew')
            except:
                message = {'status':'1','message': str(traceback.format_exc())}
                data = json.dumps(message)
                return HttpResponse(data, content_type =  "application/json")

            try:
                if not Article.objects.filter(id = idNew):
                    message = {'status':'2','message': 'Lo sentimos, este titulo no existe...'}
                    data = json.dumps(message)
                    return HttpResponse(data, content_type =  "application/json")
            except:
                message = {'status':'1','message': str(traceback.format_exc())}
                data = json.dumps(message)
                return HttpResponse(data, content_type =  "application/json")

            try:
                new = Article.objects.get(id = idNew)
                responseData = {}
                responseData['status'] = '3'
                responseData['id'] = new.id
                responseData['titulo'] = new.title
                tags = ', '.join([tags.name for tags in new.tags.all()])
                responseData['tags'] = tags
                responseData['autor'] = new.author
                responseData['contenido'] = new.body

                data = json.dumps(responseData)
                return HttpResponse(data, content_type =  "application/json")
            except:
                message = {'status':'1','message': str(traceback.format_exc())}
                data = json.dumps(message)
                return HttpResponse(data, content_type =  "application/json")

class modify_news(TemplateView):
    def post(self, request, *args, **kwargs):
        if request.is_ajax() and request.method == 'POST':
            try:
                idNewForm = request.POST.get('idNewForm')
                titulo = request.POST.get('titulo')
                tags = request.POST.get('tags')
                autor = request.POST.get('autor')
                contenido = request.POST.get('contenido')
            except:
                message = {'status':'1','message': str(traceback.format_exc())}
                data = json.dumps(message)
                return HttpResponse(data, content_type =  "application/json")

            try:
                if not Article.objects.filter(id = idNewForm):
                    message = {'status':'2','message': 'Lo sentimos, este titulo no existe...'}
                    data = json.dumps(message)
                    return HttpResponse(data, content_type =  "application/json")
            except:
                message = {'status':'1','message': str(traceback.format_exc())}
                data = json.dumps(message)
                return HttpResponse(data, content_type =  "application/json")

            try:
                if Article.objects.filter(title = titulo):
                    message = {'status':'2','message': 'Lo sentimos, este titulo ya ha siso registrado, por favor seleccione otro...'}
                    data = json.dumps(message)
                    return HttpResponse(data, content_type =  "application/json")
            except:
                message = {'status':'1','message': str(traceback.format_exc())}
                data = json.dumps(message)
                return HttpResponse(data, content_type =  "application/json")

            try:
                article = Article.objects.get(id=idNewForm)
                article.title = titulo
                article.author = autor
                article.body = contenido
                article.update_at = timezone.now()
                article.save()

                for tag in article.tags.all():
                    article.tags.remove(tag)

                tags = tags.split(',')
                for tag in tags:
                    try:
                        tag_model = Tags.objects.get(name=tag.strip().upper())
                        article.tags.add(tag_model)
                        article.save()
                    except Tags.DoesNotExist:
                        tags_model = Tags()
                        tags_model.name = tag.strip().upper()
                        tags_model.save()
                        article_model.tags.add(tags_model)
                        article_model.save()

                message = {'status':'3','message': 'Datos modificados correctamente...'}
                data = json.dumps(message)
                return HttpResponse(data, content_type =  "application/json")
            except:
                message = {'status':'1','message': str(traceback.format_exc())}
                data = json.dumps(message)
                return HttpResponse(data, content_type =  "application/json")
