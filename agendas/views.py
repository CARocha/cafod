# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from models import *
from contrapartes.models import *
from forms import *
from django.contrib.contenttypes.models import ContentType

# Create your views here.

@login_required
def crear_agenda(request):
    if request.method == 'POST':
        form = AgendaForm(request.POST, request.FILES)
        form1 = DocuForm(request.POST, request.FILES)
        if form.is_valid() and form1.is_valid():
            form_uncommited = form.save(commit=False)
            form_uncommited.user = request.user
            form_uncommited.save()

            form1_uncommitd = form1.save(commit=False)
            form1_uncommitd.content_object = form_uncommited
            form1_uncommitd.save()
            return HttpResponseRedirect('/agendas')
    else:
        form = AgendaForm()
        form1 = DocuForm()
    return render_to_response('agendas/crear_agenda.html', locals(),
    	                         context_instance=RequestContext(request))

@login_required
def editar_agenda(request, id):
    agenda = get_object_or_404(Agendas, id=id)
    agenda_type = ContentType.objects.get(app_label="foros",model="documentos")
    docu = agenda_type.get_object_for_this_type(object_id=id) 
    #docu = ContentType.objects.get_for_model(Agendas)
    if not agenda.user == request.user:
    	return HttpResponse("Usted no puede editar esta Agenda")
    if request.method == 'POST':
        form = AgendaForm(request.POST, instance = agenda)
        form1 = DocuForm(request.POST, request.FILES, instance = docu)
    	if form.is_valid():
            form_uncommited = form.save(commit=False)
            form_uncommited.user = request.user
            form_uncommited.save()

            form1_uncommitd = form1.save(commit=False)
            form1_uncommitd.content_object = form_uncommited
            form1_uncommitd.save()
            return HttpResponseRedirect('/agendas')
    else:
        form = AgendaForm(instance=agenda)
        form1 = DocuForm(instance=docu)
    return render_to_response('agendas/crear_agenda.html', locals(),
    	                         context_instance=RequestContext(request))

@login_required
def borrar_agenda(request, id):
    agenda = get_object_or_404(Agendas, pk=id)

    if agenda.user == request.user or request.user.is_superuser:
        agenda.delete()
        return redirect('/agendas')
    else:
        return redirect('/')
