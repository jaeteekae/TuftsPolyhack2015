from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add$', views.add, name='add'),
    url(r'^vote$', views.vote, name='vote'),
    url(r'^playlist$', views.playlist, name='playlist'),
    url(r'^login$', views.login, name='login'),
    url(r'^login/$', views.login, name='login'),
]