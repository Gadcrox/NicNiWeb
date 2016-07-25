# -*- coding: utf-8 -*-
# encoding=utf8
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse
#from .models import Services
import json, traceback

@login_required
def services_add_view(request):
    return render(request, 'addServices.html')
