from django.conf.urls import patterns, include, url

urlpatterns = patterns('foros.views',
    url(r'^$', 'index', name='index'),
     url(r'^crear/$', 'crear_foro', name='crear-foro'),
)
