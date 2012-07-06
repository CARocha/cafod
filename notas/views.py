# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from models import *
from agendas.models import *
from contrapartes.models import *
from forms import *
from django.contrib.contenttypes.generic import generic_inlineformset_factory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import thread
import datetime
import operator
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.sites.models import Site

# Create your views here.

def logout_page(request):
  logout(request)
  return HttpResponseRedirect('/')

def lista_notas(request):
    notas_list = Notas.objects.all().order_by('-fecha','-id')
    paises = Pais.objects.all()

    paginator = Paginator(notas_list, 4)

    page = request.GET.get('page')
    try:
        notas = paginator.page(page)
    except PageNotAnInteger:
        notas = paginator.page(1)
    except EmptyPage:
        notas = paginator.page(paginator.num_pages)

    return render_to_response('notas/notas_list.html', locals(),
                              context_instance=RequestContext(request))

def detalle_notas(request, id):
    nota = get_object_or_404(Notas, id=id)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)

        if form.is_valid():
            form_uncommited = form.save(commit=False)
            form_uncommited.user = request.user
            form_uncommited.nota = nota
            form_uncommited.save()

        return HttpResponseRedirect('/notas/%d/#cmt%d' % (nota.id,form.instance.id) )

    else:
        form = ComentarioForm()

    return render_to_response('notas/notas_detail.html', locals(),
                                 context_instance=RequestContext(request))  

def lista_notas_pais(request,id):
    notas_list = Notas.objects.filter(user__userprofile__contraparte__pais__id=id).order_by('-fecha','-id')
    paises = Pais.objects.all()
    pais_selecto = Pais.objects.get(pk=id)

    paginator = Paginator(notas_list, 4)

    page = request.GET.get('page')
    try:
        notas = paginator.page(page)
    except PageNotAnInteger:
        notas = paginator.page(1)
    except EmptyPage:
        notas = paginator.page(paginator.num_pages)

    return render_to_response('notas/notas_list.html', locals(),
                              context_instance=RequestContext(request))


def index(request):

    notas = Notas.objects.all().order_by('-fecha','-id')[:3]
    notas2 = Notas.objects.all().order_by('-fecha','-id')[3:6]
    evento = Agendas.objects.filter(publico=True).order_by('-inicio')[:3]
    paises = Pais.objects.all()
    contrapartes = Contraparte.objects.all()

    return render_to_response('index.html', locals(),
                              context_instance=RequestContext(request))

@login_required
def crear_nota(request):
    if request.method == 'POST':
        form = NotasForms(request.POST)
        form2 = FotoForm(request.POST, request.FILES)
        form3 = AdjuntoForm(request.POST, request.FILES)

    	if form.is_valid() and form2.is_valid() and form3.is_valid():
            form_uncommited = form.save(commit=False)
            form_uncommited.user = request.user
            form_uncommited.save()
            if form2.cleaned_data['nombre_img'] != '':
                form2_uncommited = form2.save(commit=False)
                form2_uncommited.content_object = form_uncommited
                form2_uncommited.save()
            if form3.cleaned_data['nombre_doc'] != '':    
                form3_uncommited = form3.save(commit=False)
                form3_uncommited.content_object = form_uncommited
                form3_uncommited.save()

            thread.start_new_thread(notify_all_notas, (form_uncommited,))
            return HttpResponseRedirect('/foros/privado/nota/')
    else:
        form = NotasForms()
        form2 = FotoForm()
        form3 = AdjuntoForm()

    return render_to_response('notas/crear_nota.html', locals(),
    	                         context_instance=RequestContext(request))

@login_required
def editar_nota(request, id):
    nota = get_object_or_404(Notas, id=id)
    NotaFormSet = generic_inlineformset_factory(Imagen, extra=5, max_num=5)
    Nota2FormSet = generic_inlineformset_factory(Documentos, extra=5, max_num=5)
    form2 = NotaFormSet(instance=nota)
    form3 = Nota2FormSet(instance=nota)

    if not nota.user == request.user and not request.user.is_superuser:
    	return HttpResponse("Usted no puede editar esta nota")

    if request.method == 'POST':
        form = NotasForms(request.POST, instance=nota)
        form2 = NotaFormSet(data=request.POST, files=request.FILES, instance=nota)
        form3 = Nota2FormSet(data=request.POST, files=request.FILES, instance=nota)

    	if form.is_valid() and form2.is_valid() and form3.is_valid():
            nota.titulo = request.POST['titulo']
            nota.contenido = request.POST['contenido']
            nota.fecha = datetime.datetime.now()
            nota.user = request.user
            nota.save()
            #salvando inline
            form2.save()
            form3.save()
            return HttpResponseRedirect('%s?shva=ok' % nota.get_absolute_url())
    else:
        form = NotasForms(instance=nota)
        form2 = NotaFormSet(instance=nota)
        form3 = Nota2FormSet(instance=nota)

    return render_to_response('notas/editar_nota.html', locals(),
    	                         context_instance=RequestContext(request))

@login_required
def borrar_nota(request, id):
    nota = get_object_or_404(Notas, pk=id)

    if nota.user == request.user or request.user.is_superuser:
        nota.delete()
        #return redirect('/notas')
        return HttpResponseRedirect('/notas/?shva=erase')
    else:
        return redirect('/')

def notify_all_notas(notas):
    site = Site.objects.get_current()
    users = User.objects.all() #.exclude(username=foros.contraparte.username)
    contenido = render_to_string('notas/notify_new_nota.txt', {'nota': notas,
                                 'url': '%s/notas/%s' % (site, notas.id),
                                 #'url_aporte': '%s/foros/ver/%s/#aporte' % (site, foros.id),
                                 })
    send_mail('Nueva Nota en CAFOD', contenido, 'cafod@cafodca.org', [user.email for user in users if user.email])

@login_required
def comentar_nota(request, id):
    nota = get_object_or_404(Notas, id=id)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)

        if form.is_valid():
            form_uncommited = form.save(commit=False)
            form_uncommited.user = request.user
            form_uncommited.nota = nota
            form_uncommited.save()

        return HttpResponseRedirect('/notas/ver/%d' % nota.id)

    else:
        form = ComentarioForm()

    return render_to_response('privados/ver_nota.html', locals(),
                                 context_instance=RequestContext(request))  
