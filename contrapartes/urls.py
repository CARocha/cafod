from django.conf.urls.defaults import *
from django.views.generic import ListView, DetailView
from models import Contraparte

urlpatterns = patterns('contrapartes.views',
    url(r'^$', ListView.as_view(model=Contraparte, 
    	                        template_name="contraparte/contraparte_list.html"),
                                name="contraparte-list"),
    url(r'^(?P<pk>\d+)/$', DetailView.as_view(model=Contraparte, 
    	                                        template_name='notas/contraparte_detail.html'),
                                                name='contraparte-detail'),
    url(r'^crear/$', 'crear_contraparte', name="crear-contraparte"),
    url(r'^editar/(?P<id>\d+)/$', 'editar_contraparte', name='editar-contraparte'),
    url(r'^borrar/(?P<id>\d+)/$', 'borrar_contraparte', name='borrar-contraparte'),
    )