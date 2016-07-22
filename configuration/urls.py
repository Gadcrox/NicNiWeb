from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.configuration_add_view, name='configuration.add'),
    url(r'^add/$', views.configuration_add_view, name='configuration.add'),
    #url(r'^modify/$', views.profile_modify_view, name='accounts.modify'),
    #url(r'^insert/$', create_account.as_view()),
    #url(r'^view_account/$', view_account.as_view()),
    url(r'^update/$', views.modify_configuration.as_view()),

]
