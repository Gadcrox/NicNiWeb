from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.news_add_view, name='news.add'),
    url(r'^add/$', views.news_add_view, name='news.add'),
    #url(r'^modify/$', views.profile_modify_view, name='accounts.modify'),
    url(r'^insert/$', views.create_news.as_view()),
    #url(r'^view_account/$', view_account.as_view()),
    #url(r'^update/$', modify_account.as_view()),

]
