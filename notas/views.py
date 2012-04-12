# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from models import *
from contrapartes.models import *
from forms import *

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
    if request.method == 'POST':
    	form = NotasForms(request.POST, request.FILES)
        form1 = FotoForm(request.POST, request.FILES)
        form2 = AdjuntoForm(request.POST, request.FILES)
    	if form.is_valid() and form1.is_valid() and form2.is_valid():
            form_uncommited = form.save(commit=False)
            form_uncommited.user = request.user
            form_uncommited.save()

            form1_uncommited = form1.save(commit=False)
            form1_uncommited.content_object = form_uncommited
            form1_uncommited.save()

            form2_uncommited = form2.save(commit=False)
            form2_uncommited.content_object = form_uncommited
            form2_uncommited.save()

            return HttpResponseRedirect('/notas')
    else:
    	form = NotasForms()
        form1 = FotoForm()
        form2 = AdjuntoForm()
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
    