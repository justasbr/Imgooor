from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'gifs.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^gifai/', include('gifai.urls', namespace='gifai')),
                       url(r'^anagram/', include('anagram.urls', namespace='anagram')),
                       url(r'^admin/', include(admin.site.urls)),
)
