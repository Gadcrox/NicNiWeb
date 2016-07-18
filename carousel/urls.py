from django.conf.urls import url

from . import views
#from .views import create_account, view_account, modify_account

urlpatterns = [
    url(r'^$', views.carousel_view_view, name='carousel.view'),
    url(r'^view/$', views.carousel_view_view, name='carousel.view'),
    #url(r'^modify/$', views.profile_modify_view, name='accounts.modify'),
    #url(r'^insert/$', create_account.as_view()),
    #url(r'^view_account/$', view_account.as_view()),
    #url(r'^update/$', modify_account.as_view()),

]
