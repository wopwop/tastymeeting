from django.conf.urls.defaults import patterns, include, url
import os

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Import views
from tastymeeting.views.home import *
from tastymeeting.views.meals import *
from tastymeeting.views.profile import *


# Site media folder path
site_media = os.path.join(os.path.dirname(__file__), 'site_media')
upload = os.path.join(os.path.dirname(__file__), 'upload')


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tastymeeting.views.home', name='home'),
    # url(r'^tastymeeting/', include('tastymeeting.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': site_media}),
    url(r'^upload/(?P<path>.*)$', 'django.views.static.serve', {'document_root':upload}),
    
    # Home signup and login urls
    url(r'^$',home),
    url(r'^login/$',login),
    url(r'^signup/$', signup),
    url(r'^fbconnect/$',fbconnect),
    url(r'^logout/$',logout),
    
    # Meals urls
    url(r'^meals/(?P<location>\w+)/$',meals),
    url(r'^restaurant/(?P<restaurant>[-\w]+)/(?P<meal_id>\d+)/$', meal_details),
    
    # Profile urls
    url(r'^settings/$', settings_profile),
    url(r'^settings/password/$', settings_pass),
    
    
    
)
