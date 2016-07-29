from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.news_add_view, name='news.add'),
    url(r'^add/$', views.news_add_view, name='news.add'),
    url(r'^modify/$', views.news_modify_view, name='news.modify'),
    url(r'^insert/$', views.create_news.as_view()),
    url(r'^view_new/$', views.view_new.as_view()),
    url(r'^update/$', views.modify_news.as_view()),

]
