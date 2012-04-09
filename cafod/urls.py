from django.conf.urls import patterns, include, url
from settings import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cafod.views.home', name='home'),
    # url(r'^cafod/', include('cafod.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^accounts/logout/$', 'notas.views.logout_page'),
    (r'^$', 'notas.views.index'),
    #url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'registration/login.html'}, 
        #name='user-login'),
    #url(r'^logout/$', 'notas.views.logout_page', name="logout"),
    url(r'^notas/', include('notas.urls')),
    url(r'^contrapartes/', include('contrapartes.urls')),
    url(r'^agendas/', include('agendas.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tagging_autocomplete/', include('tagging_autocomplete.urls')),
    url(r'^foro/', include('foros.urls')),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()

if DEBUG:
    urlpatterns += patterns('',
                (r'^uploads/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
                )