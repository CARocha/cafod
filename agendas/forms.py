from django.db import models
from django.forms import ModelForm
from django import forms
from models import *
from foros.models import *
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from utils import *

class AgendaForm(ModelForm):
    class Meta:
    	model = Agendas
    	exclude = ('user',)

class DocuForm(forms.ModelForm):
    adjunto = forms.FileField()
    class Meta:
    	model = Documentos
    	exclude = ('content_type', 'object_id', 'content_object',)