# -*- coding: utf-8 -*-
# encoding=utf8
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User
from django.http import HttpResponse
import json, traceback
from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.conf import settings
# Create your views here.
@login_required
def profile_add_view(request):
    return render(request, 'add.html')

@login_required
def profile_modify_view(request):
    user_list = User.objects.all().order_by('username')
    context = { 'user_list': user_list }
    return render(request, 'modify.html', context)

class view_account(TemplateView):
    def post(self, request, *args, **kwargs):
        if request.is_ajax() and request.method == 'POST':
            try:
                idAccount = request.POST.get('idAccount')
            except:
                message = {'status':'2','message': str(traceback.format_exc())}
                data = json.dumps(message)
                return HttpResponse(data, content_type =  "application/json")

            try:
                if not User.objects.filter(id = idAccount):
                    message = {'status':'1','message': 'Lo sentimos, este nombre de usuario no existe...'}
                    data = json.dumps(message)
                    return HttpResponse(data, content_type =  "application/json")
            except:
                    message = {'status':'2','message': str(traceback.format_exc())}
                    data = json.dumps(message)
                    return HttpResponse(data, content_type =  "application/json")

            try:
                user = User.objects.get(id = idAccount)
                response_data = {}
                response_data['status'] = '3'
                response_data['id'] = user.id
                response_data['username'] = user.username
                response_data['firstname'] = user.first_name
                response_data['lastname'] = user.last_name
                response_data['is_superuser'] = user.is_superuser
                response_data['is_active'] = user.is_active

                data = json.dumps(response_data)
                return HttpResponse(data, content_type =  "application/json")
            except:
                message = {'status':'2','message': str(traceback.format_exc())}
                data = json.dumps(message)
                return HttpResponse(data, content_type =  "application/json")

class create_account(TemplateView):

    def post(self, request, *args, **kwargs):
        if request.is_ajax() and request.method == 'POST':

            try:
                username = request.POST.get('username')
                firstname = request.POST.get('firstname')
                lastname = request.POST.get('lastname')
                admin = bool(request.POST.get('admin'))
                active = bool(request.POST.get('active'))
                newpassword = request.POST.get('password')

            except:
                message = {'status':'2','message': str(traceback.format_exc())}
                data = json.dumps(message)
                return HttpResponse(data, content_type =  "application/json")

            try:
                if User.objects.filter(username=username):
                    message = {'status':'1','message': 'Lo sentimos, este nombre de usuario ya ha sido registrado, por favor seleccione otro...'}
                    data = json.dumps(message)
                    return HttpResponse(data, content_type =  "application/json")
            except:
                    message = {'status':'2','message': str(traceback.format_exc())}
                    data = json.dumps(message)
                    return HttpResponse(data, content_type =  "application/json")

            try:
                user_model = User.objects.create_user(username=username, password=newpassword)

                user_model.first_name = firstname
                user_model.last_name = lastname
                user_model.is_active = active
                user_model.is_superuser = admin
                user_model.date_joined = timezone.now()
                user_model.is_staff = admin
                user_model.save()


                message = {'status':'3','message': 'Datos ingresados satisfactoriamente.'}
                data = json.dumps(message)
                return HttpResponse(data, content_type =  "application/json")
            except:
                message = {'status':'2','message': str(traceback.format_exc())}
                data = json.dumps(message)
                return HttpResponse(data, content_type =  "application/json")


class modify_account(TemplateView):

    def post(self, request, *args, **kwargs):
        if request.is_ajax() and request.method == 'POST':
            try:
                username = request.POST.get('username')
                firstname = request.POST.get('firstname')
                lastname = request.POST.get('lastname')
                admin = bool(request.POST.get('admin'))
                active = bool(request.POST.get('active'))
                newpassword = request.POST.get('password')
                confirmpassword = request.POST.get('confirmpassword')
            except:
                message = {'status':'2','message': str(traceback.format_exc())}
                data = json.dumps(message)
                return HttpResponse(data, content_type =  "application/json")

            try:
                user_model = User.objects.get(username = username)
            except User.DoesNotExist:
                message = {'status':'1','message': 'Lo sentimos, este nombre de usuario no ha sido encontrado...'}
                data = json.dumps(message)
                return HttpResponse(data, content_type =  "application/json")

            try:
                user_model.first_name = firstname
                user_model.last_name = lastname
                user_model.is_superuser = admin
                user_model.is_active = active
                user_model.is_staff = admin
                response_data = {}

                if newpassword:
                    if newpassword == confirmpassword:
                        user_model.set_password( newpassword )

                        user_model.save()
                        response_data['status'] = '3'
                        response_data['message'] = 'Datos modificados satisfactoriamente..'
                        response_data['first_name'] = firstname
                        response_data['is_superuser'] = admin
                        response_data['is_active'] = active
                        response_data['last_name'] = lastname
                        data = json.dumps(response_data)
                        return HttpResponse(data, content_type =  "application/json")
                    else:
                        message = {'status':'4','message': 'La contraseña tiene que coincidir'}
                        data = json.dumps(message)
                        return HttpResponse(data, content_type =  "application/json")

                else:
                    user_model.save()
                    response_data['status'] = '3'
                    response_data['message'] = 'Datos modificados satisfactoriamente..'
                    response_data['first_name'] = firstname
                    response_data['is_superuser'] = admin
                    response_data['is_active'] = active
                    response_data['last_name'] = lastname
                    data = json.dumps(response_data)
                    return HttpResponse(data, content_type =  "application/json")



            except:
                message = {'status':'2','message': str(traceback.format_exc())}
                data = json.dumps(message)
                return HttpResponse(data, content_type =  "application/json")
