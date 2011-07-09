from django.conf.urls.defaults import patterns, include, url
import os

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Import views
from tastymeeting.views.home import *


# Site media folder path
site_media = os.path.join(os.path.dirname(__file__), 'site_media')



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tastymeeting.views.home', name='home'),
    # url(r'^tastymeeting/', include('tastymeeting.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': site_media}),
    url(r'^$',home),
    url(r'^loginbox/$',loginbox),
    url(r'^signup/$', signup)
    
)
