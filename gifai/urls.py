from django.conf.urls import patterns, url
from gifai import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<gif_id>\d+)/$', views.detail, name='detail'),
	url(r'^(?P<gif_id>\d+)/vote/$', views.vote, name ='vote'),
)
