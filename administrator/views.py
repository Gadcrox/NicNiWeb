# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.conf import settings

@login_required
# Create your views here.
def home_view(request):
    return render(request, 'administrator.html')


def login_view(request):
    if request.user.is_authenticated():
        return redirect(reverse('administrador.index'))

    mensaje = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = bool(request.POST.get('remember'))
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                if not remember:
                    settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = True
                else:
                    settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = False
                login(request, user)
                return redirect(reverse('administrator.login'))
            else:
                # Redireccionar informando que la cuenta esta inactiva
                pass
        mensaje = 'false'
        print mensaje
    return render(request, 'login.html', {'mensaje': mensaje})

def logout_view(request):
    logout(request)
    print 'salir'
    return redirect(reverse('administrator.login'))
