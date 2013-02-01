# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from models import *
from forms import *
from notas.models import *
from agendas.models import *
from django.contrib.sites.models import Site
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
import operator
import thread
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
#def contrapartes_index(request):
#    contra = Contraparte.objects.all()
#    return render_to_response('contrapartes/contraparte_index.html', locals(),
#                                 context_instance=RequestContext(request))


def detalle_contraparte(request,id):
    contra = get_object_or_404(Contraparte, id=id)
    notas = Notas.objects.filter(user__userprofile__contraparte__id=id).order_by('-fecha')
    return render_to_response('contrapartes/contraparte_detail.html', locals(),
                                 context_instance=RequestContext(request))

@login_required
def crear_contraparte(request):
    form = ContraparteForms(request.POST, request.FILES)
    if request.method == 'POST':
    	if form.is_valid():
            form_uncommited = form.save(commit=False)
            form_uncommited.user = request.user
            form_uncommited.save()
            return HttpResponseRedirect('/')
    else:
    	form = ContraparteForms()
    return render_to_response('contrapartes/crear_contraparte.html', locals(),
    	                         context_instance=RequestContext(request))

@login_required
def editar_contraparte(request, id):
    contra = get_object_or_404(Contraparte, id=id)
    user_ids = UserProfile.objects.filter(contraparte__id=contra.id).values_list('user__id', flat=True)

    if not request.user.id in user_ids:
        if not request.user.is_superuser:
            return HttpResponse("Usted no puede editar esta Contraparte")

    if request.method == 'POST':
        form = ContraparteForms(data=request.POST, 
                                instance=contra, 
                                files=request.FILES)
        if form.is_valid():
            form_uncommited = form.save(commit=False)
            form_uncommited.user = request.user
            form_uncommited.save()
            return HttpResponseRedirect('%s?shva=ok' % '/foros/perfil/')
    else:
        form = ContraparteForms(instance=contra)
    return render_to_response('contrapartes/crear_contraparte.html', locals(),
                                 context_instance=RequestContext(request))

# @login_required
# def borrar_contraparte(request, id):
#     contra = get_object_or_404(Contraparte, pk=id)
#     usuarios = UserProfile.objects.filter(contraparte_id=contra.id)

#     nombres = []
#     for obj in usuarios:
#         nombres.append(obj.user.username)

#     if request.user.username in [i for i in nombres] or request.user.is_superuser:
#         contra.delete()
#         return redirect('contraparte-list')
#     else:
#         return redirect('/')

@login_required
def editar_usuario_perfil(request):
    #usuario = get_object_or_404(User, id=id)

    if request.method == 'POST':
        form = UserForm(data=request.POST, instance=request.user)
        form1 = UserProfileForm(data=request.POST, instance=request.user.userprofile, files=request.FILES)
        if form.is_valid() and form1.is_valid():
            form.save()
            form1.save()
            #form_uncommited = form.save(commit=False)
            #form_uncommited.user = request.user
            #form_uncommited.save()

            return HttpResponseRedirect('/foros/perfil')
    else:
        form = UserForm(instance=request.user)
        form1 = UserProfileForm(instance=request.user.userprofile)
    return render_to_response('contrapartes/editar_usuario.html', locals(),
                                 context_instance=RequestContext(request))

@login_required
def enviar_mensaje(request):
    mensaje = Mensajero.objects.filter(user=request.user).order_by('-id')
    paginator = Paginator(mensaje, 5)
    page = request.GET.get('page')
    try:
        mensajes = paginator.page(page)
    except PageNotAnInteger:
        mensajes = paginator.page(1)
    except EmptyPage:
        mensajes = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            #form.save()
            form_uncommited = form.save(commit=False)
            form_uncommited.usuario = request.user
            #form_uncommited.user = form.cleaned_data['user']
            form_uncommited.save()
            form.save_m2m()

            thread.start_new_thread(notify_user_mensaje, (form_uncommited, ))
            guardado=1

            return HttpResponseRedirect('/contrapartes/mensaje/ver/?guardado=ok')

    else:
        form = MensajeForm()
    return render_to_response('contrapartes/mensaje.html', locals(),
                                context_instance=RequestContext(request))

def notify_user_mensaje(mensaje):
    site = Site.objects.get_current()
    contenido = render_to_string('contrapartes/notify_new_mensaje.html', {
                                   'mensajes': mensaje,
                                   'url': '%s/contrapartes/mensaje/ver/' % (site,)
                                    })
    msg = EmailMultiAlternatives('Nuevo mensaje CAFOD', contenido, 'cafod@cafodca.org', [user.email for user in mensaje.user.all() if user.email])
    msg.attach_alternative(contenido, "text/html")
    msg.send()
    #send_mail('Nuevo mensaje CAFOD', contenido, 'cafod@cafodca.org', [user.email for user in mensaje.user.all() if user.email])

@login_required
def estadisticas(request):
    total = {}
    for usuario in User.objects.all():
        foro = Foros.objects.filter(contraparte=usuario).count()
        nota = Notas.objects.filter(user=usuario).count()
        aporte = Aportes.objects.filter(user=usuario).count()
        comentario = Comentarios.objects.filter(usuario=usuario).count()
        #Estadisticas sobre documentos,imagenes,videos,audios

        lista_documentos_notas = []
        lista_imagenes_notas = []
        for documentos in Notas.objects.filter(user=usuario):
            for numero in documentos.adjuntos.all():
                lista_documentos_notas.append(numero)
            for foto in documentos.fotos.all():
                lista_imagenes_notas.append(foto)

        lista_documentos_eventos = []
        for eventos in Agendas.objects.filter(user=usuario):
            for numero in eventos.adjunto.all():
                lista_documentos_eventos.append(numero)

        lista_documentos_foros = []
        lista_imagenes_foros = []
        lista_videos_foros = []
        lista_audios_foros = []
        for foros in Foros.objects.filter(contraparte=usuario):
            for numero in foros.documentos.all():
                lista_documentos_foros.append(numero)
            for imagen in foros.fotos.all():
                lista_imagenes_foros.append(imagen)
            for video in foros.video.all():
                lista_videos_foros.append(video)
            for audio in foros.audio.all():
                lista_audios_foros.append(audio)

        lista_documentos_aporte = []
        lista_imagen_aporte = []
        lista_videos_aporte = []
        lista_audios_aporte = []
        for aportes in Aportes.objects.filter(user=usuario):
            for numero in aportes.adjuntos.all():
                lista_documentos_aporte.append(numero)
            for imagen in aportes.fotos.all():
                lista_imagen_aporte.append(imagen)
            for video in aportes.video.all():
                lista_videos_aporte.append(video)
            for audio in aportes.audio.all():
                lista_audios_aporte.append(audio)


        documentos = len(lista_documentos_notas) + len(lista_documentos_eventos) + \
        len(lista_documentos_foros) + len(lista_documentos_aporte)
        imagenes = len(lista_imagenes_notas) + len(lista_imagenes_foros) + \
        len(lista_imagen_aporte)
        #documentos = foro2.aggregate(documentos=Count('documentos'))['documentos']
        #imagenes = aporte2.aggregate(imagenes=Count('fotos'))['imagenes']
        videos = len(lista_videos_foros) + len(lista_videos_aporte)
        audios = len(lista_audios_foros) + len(lista_audios_aporte)
        total[usuario] = (nota,foro,aporte,comentario,documentos,imagenes,videos,audios)

    return render_to_response('privados/estadisticas.html', locals(),
                                 context_instance=RequestContext(request))    
