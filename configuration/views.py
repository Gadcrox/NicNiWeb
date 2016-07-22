# -*- coding: utf-8 -*-
# encoding=utf8
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse
from .models import Configuration
import json, traceback

# Create your views here.
@login_required
def configuration_add_view(request):
    configuration = Configuration.objects.first()
    context = {'configuration': configuration}
    return render(request, 'configuration.html', context)


class modify_configuration(TemplateView):
    def post(self,request, *args, **kwargs):
        if request.is_ajax() and request.method == 'POST':
            try:
                historia = request.POST.get('historia')
                concepto = request.POST.get('concepto')
                telefono = request.POST.get('telefono')
                correo = request.POST.get('correo')
                direccion = request.POST.get('direccion')
                codigo_postal = request.POST.get('codigo_postal')
                facebook = request.POST.get('facebook')
                google_plus = request.POST.get('google_plus')
                linkedin = request.POST.get('linkedin')
                instagram = request.POST.get('instagram')
                twitter = request.POST.get('twitter')



            except:
                message = {'status':'1','message': str(traceback.format_exc())}
                data = json.dumps(message)
                return HttpResponse(data, content_type =  "application/json")

            try:
                configuration_model = Configuration.objects.first()
                if configuration_model is not None:
                    configuration_model.historia = historia
                    configuration_model.concepto = concepto
                    configuration_model.telefono = telefono
                    configuration_model.correo = correo
                    configuration_model.direccion = direccion
                    configuration_model.codigo_postal = codigo_postal
                    configuration_model.facebook = facebook
                    configuration_model.google_plus = google_plus
                    configuration_model.linkedin = linkedin
                    configuration_model.instagram = instagram
                    configuration_model.twitter = twitter
                    configuration_model.save()
                    response_data = {}
                    response_data['status'] = '3'
                    response_data['message'] = 'Datos modificados satisfactoriamente..'
                    data = json.dumps(response_data)
                    return HttpResponse(data, content_type =  "application/json")
                else:
                    configuration_model = Configuration()
                    configuration_model.historia = historia
                    configuration_model.concepto = concepto
                    configuration_model.telefono = telefono
                    configuration_model.correo = correo
                    configuration_model.direccion = direccion
                    configuration_model.codigo_postal = codigo_postal
                    configuration_model.facebook = facebook
                    configuration_model.google_plus = google_plus
                    configuration_model.linkedin = linkedin
                    configuration_model.instagram = instagram
                    configuration_model.twitter = twitter
                    configuration_model.save()
                    response_data = {}
                    response_data['status'] = '3'
                    response_data['message'] = 'Datos modificados satisfactoriamente..'
                    data = json.dumps(response_data)
                    return HttpResponse(data, content_type =  "application/json")
            except Configuration.DoesNotExist:
                message = {'status':'2','message': 'Registro no encontrado'}
                data = json.dumps(message)
                return HttpResponse(data, content_type =  "application/json")
