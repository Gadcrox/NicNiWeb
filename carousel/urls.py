from django.conf.urls import url

from . import views
from .views import create_new_item, view_item

urlpatterns = [
    url(r'^$', views.carousel_view_view, name='carousel.view'),
    url(r'^view/$', views.carousel_view_view, name='carousel.view'),
    #url(r'^modify/$', views.profile_modify_view, name='accounts.modify'),
    url(r'^insert/$', create_new_item.as_view()),
    url(r'^view_item/$', view_item.as_view()),
    #url(r'^update/$', modify_account.as_view()),

]
