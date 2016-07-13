from django.conf.urls import url

from . import views
from .views import create_account

urlpatterns = [
    url(r'^$', views.profile_add_view, name='accounts.add'),
    url(r'^add/$', views.profile_add_view, name='accounts.add'),
    url(r'^insert/$', create_account.as_view()),
#    url(r'^update/$', modify_account.as_view()),
#    url(r'^modify/$', profile_modify_view, name='accounts.modify'),
]
