from django.db import models
from django.forms import ModelForm
from django import forms
from models import *
from foros.models import *

class AgendaForm(ModelForm):
    class Meta:
    	model = Agendas
    	exclude = ('user',)

class DocuForm(ModelForm):
    class Meta:
    	model = Documentos
    	exclude = ('content_type', 'object_id', 'content_object',)