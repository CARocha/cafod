import operator
import thread
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.template.loader import render_to_string
from forms import *
from models import *
from tagging.models import Tag
from tagging.models import TaggedItem


# Create your views here.

def index(request):
    a = "Hola pues...!!!"
    return render_to_response('index.html', locals(), 
    	           context_instance=RequestContext(request))

#@login_required
def crear_foro(request):
    if request.method == 'POST':
        form = ForosForm(request.POST)
        if form.is_valid():
            obj = Foros()
            obj.nombre = request.POST['nombre']
            obj.creacion = datetime.datetime.now()
            obj.apertura = datetime.datetime.now()
            obj.cierre = datetime.datetime.now()
            obj.fecha_skype = datetime.datetime.now()
            obj.memoria = datetime.datetime.now()
            obj.contenido = request.POST['contenido']
            obj.contraparte = request.user
            obj.save()
            #if form.cleaned_data['notify']:
              #  thread.start_new_thread(notify_all, (obj,))
            #return HttpResponseRedirect('/foro/?tab=latest')
    else:
        form = ForosForm()
    return render_to_response('foros/crear_foro.html', RequestContext(request, locals()))