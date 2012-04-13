# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from models import *
from contrapartes.models import *
from forms import *
from django.contrib.contenttypes.generic import generic_inlineformset_factory

# Create your views here.

def logout_page(request):
  logout(request)
  return HttpResponseRedirect('/')

def index(request):

    notas = Notas.objects.all().order_by('-fecha')[:4]

    contra = {}
    for pais in Pais.objects.all():
    	for contraparte in Contraparte.objects.filter(pais__id=pais.id):
    	    	if not pais.nombre in contra.keys():
    	    	    contra[pais.nombre] = [[contraparte.nombre],]
    	    	else:
    	    	    contra[pais.nombre].append([contraparte.nombre])

    return render_to_response('index.html', locals(),
                              context_instance=RequestContext(request))

@login_required
def crear_nota(request):
    
    NotaFormset = generic_inlineformset_factory(Imagen, extra=2)
    
    if request.method == 'POST':
        form = NotasForms(request.POST)
        formset = NotaFormset(request.POST, request.FILES)
    	if form.is_valid() and formset.is_valid():
            form_uncommited = form.save(commit=False)
            form_uncommited.user = request.user
            form_uncommited.save()

            formset = NotaFormset(request.POST) 
            #formset_uncommited = formset.save(commit=False)
            #formset_uncommited.content_object = form_uncommited
            #formset_uncommited.save()
            formset.save()
            return HttpResponseRedirect('/notas')
    else:
        form = NotasForms()
        formset = NotaFormset()

    return render_to_response('notas/crear_nota.html', locals(),
    	                         context_instance=RequestContext(request))

@login_required
def editar_nota(request, id):
    nota = get_object_or_404(Notas, id=id)
    if not nota.user == request.user:
    	return HttpResponse("Usted no puede editar esta nota")
    if request.method == 'POST':
    	form = NotasForms(request.POST, instance=nota)
    	if form.is_valid():
            nota.titulo = request.POST['titulo']
            nota.contenido = request.POST['contenido']
            nota.fecha = datetime.datetime.now()
            nota.user = request.user
            nota.save()
            return HttpResponseRedirect('/notas')
    else:
    	form = NotasForms(instance=nota)
    return render_to_response('notas/crear_nota.html', locals(),
    	                         context_instance=RequestContext(request))

@login_required
def borrar_nota(request, id):
    nota = get_object_or_404(Notas, pk=id)

    if nota.user == request.user or request.user.is_superuser:
        nota.delete()
        return redirect('/notas')
    else:
        return redirect('/')
    