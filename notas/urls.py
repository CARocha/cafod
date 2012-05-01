from django.conf.urls.defaults import *
from django.views.generic import ListView, DetailView
from models import Notas

urlpatterns = patterns('notas.views',
    #url(r'^$', ListView.as_view(model=Notas, paginate_by=2, 
	#			  template_name="notas/notas_list.html"),
	#			  name='notas_list'),
    url(r'^$', 'lista_notas', name="notas_list"),
    url(r'^pais/(?P<id>\d+)/$', 'lista_notas_pais', name="notas_list"),
    #url(r'^(?P<pk>\d+)/$', 'detalle_notas', name='notas_detail'),
    url(r'^(?P<pk>\d+)/$', DetailView.as_view(model=Notas, 
						   template_name='notas/notas_detail.html'),
                                                name='notas_detail'),
    url(r'^crear/$', 'crear_nota', name="crear-nota"),
    url(r'^editar/(?P<id>\d+)/$', 'editar_nota', name='editar-nota'),
    url(r'^borrar/(?P<id>\d+)/$', 'borrar_nota', name='borrar-nota'),
    )