from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = patterns('',
                       url(r'^$', RedirectView.as_view(pattern_name='gifai:index')),
                       url(r'^gifai/', include('gifai.urls', namespace='gifai')),
                       url(r'^admin/', include(admin.site.urls)),
)