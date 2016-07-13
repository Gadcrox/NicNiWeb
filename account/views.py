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
                message = {'status':'False','message': str(traceback.format_exc())}
                data = json.dumps(message)
                return HttpResponse(data, content_type =  "application/json")

            try:
                if User.objects.filter(username=username):
                    message = {'status':'1','message': 'Lo sentimos, este nombre de usuario ya ha siso registrado, por favor seleccione otro...'}
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
                message = {'status':'False','message': str(traceback.format_exc())}
                data = json.dumps(message)
                return HttpResponse(data, content_type =  "application/json")
