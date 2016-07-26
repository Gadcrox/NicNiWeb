# -*- coding: utf-8 -*-
# encoding=utf8
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse
from .models import Services
import json, traceback

@login_required
def services_add_view(request):
    return render(request, 'addServices.html')

@login_required
def service_modify_view(request):
    services_list = Services.objects.all().order_by('titulo')
    context = {'services_list': services_list}
    return render(request, 'modifyServices.html', context)

class view_service_view(TemplateView):
    def post(self, request, *args, **kwargs):
        if request.is_ajax() and request.method == 'POST':
            try:
                idService = request.POST.get('idService')
            except:
                message = {'status':'1','message': str(traceback.format_exc())}
                data = json.dumps(message)
                return HttpResponse(data, content_type =  "application/json")

            try:
                if not Services.objects.filter(id = idService):
                    message = {'status':'2','message': 'Lo sentimos, este servicio no existe...'}
                    data = json.dumps(message)
                    return HttpResponse(data, content_type =  "application/json")
            except:
                message = {'status':'1','message': str(traceback.format_exc())}
                data = json.dumps(message)
                return HttpResponse(data, content_type =  "application/json")

            try:
                service = Services.objects.get(id = idService)
                response_data = {}
                response_data['status'] = '3'
                response_data['id'] = service.id
                response_data['titulo'] = service.titulo
                response_data['descripcion'] = service.descripcion
                data = json.dumps(response_data)
                return HttpResponse(data, content_type =  "application/json")
            except:
                message = {'status':'1','message': str(traceback.format_exc())}
                data = json.dumps(message)
                return HttpResponse(data, content_type =  "application/json")

class create_new_service(TemplateView):
    def post(self, request, *args, **kwargs):
        if request.is_ajax() and request.method == 'POST':
            try:
                titulo = request.POST.get('titulo')
                descripcion = request.POST.get('descripcion')
            except:
                message = {'status':'1','message': str(traceback.format_exc())}
                data = json.dumps(message)
                return HttpResponse(data, content_type =  "application/json")

            try:
                if Services.objects.filter(titulo = titulo):
                    message = {'status':'2','message': 'Lo sentimos, este servicio ya ha sido registrado...'}
                    data = json.dumps(message)
                    return HttpResponse(data, content_type =  "application/json")
            except:
                message = {'status':'1','message': str(traceback.format_exc())}
                data = json.dumps(message)
                return HttpResponse(data, content_type =  "application/json")

            try:
                service_model = Services()
                service_model.titulo = titulo
                service_model.descripcion = descripcion
                service_model.save()

                message = {'status':'3','message': 'Datos ingresados satisfactoriamente.'}
                data = json.dumps(message)
                return HttpResponse(data, content_type =  "application/json")
            except:

                message = {'status':'1','message': str(traceback.format_exc())}
                data = json.dumps(message)
                return HttpResponse(data, content_type =  "application/json")

class modify_service(TemplateView):
    def post(self, request, *args, **kwargs):
        if request.is_ajax() and request.method == 'POST':
            try:
                idServiceForm = request.POST.get('idServiceForm')
                titulo = request.POST.get('titulo')
                descripcion = request.POST.get('descripcion')
            except:
                message = {'status':'1','message': str(traceback.format_exc())}
                data = json.dumps(message)
                return HttpResponse(data, content_type =  "application/json")

            try:
                if not Services.objects.filter(id = idServiceForm):
                    message = {'status':'2','message': 'Lo sentimos, este servicio no existe...'}
                    data = json.dumps(message)
                    return HttpResponse(data, content_type =  "application/json")
            except:
                message = {'status':'1','message': str(traceback.format_exc())}
                data = json.dumps(message)
                return HttpResponse(data, content_type =  "application/json")

            try:
                service = Services.objects.get(id = idServiceForm)
                service.titulo = titulo
                service.descripcion = descripcion
                service.save()
                response_data = {}
                response_data['status'] = '3'
                response_data['message'] = "Datos modificados correctamente"

                data = json.dumps(response_data)
                return HttpResponse(data, content_type =  "application/json")
            except:
                message = {'status':'1','message': str(traceback.format_exc())}
                data = json.dumps(message)
                return HttpResponse(data, content_type =  "application/json")
