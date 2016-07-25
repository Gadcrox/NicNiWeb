from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index_view, name='index.index'),
    url(r'^historia/$', views.history_view, name='historia.index'),
    url(r'^contact/$', views.contact_view, name='contactenos.index'),
]
