from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.services_add_view, name='services.add'),
    url(r'^add/$', views.services_add_view, name='services.add'),
    url(r'^modify/$', views.service_modify_view, name='services.modify'),
    url(r'^insert/$', views.create_new_service.as_view()),
    url(r'^view_service/$', views.view_service_view.as_view()),
    url(r'^update/$', views.modify_service.as_view()),


]
