from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index_view, name='index.index'),
    url(r'^historia/$', views.history_view, name='historia.index'),
    url(r'^contactenos/$', views.contact_view, name='contactenos.index'),
    url(r'^servicio/(?P<slug>[-\w]+)/$', views.service_index_view, name='service.index'),
    url(r'^noticias/(?P<slug>[-\w]+)/$', views.new_index_view, name='new.index'),

]
