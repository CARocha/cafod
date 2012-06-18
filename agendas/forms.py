# -*- coding: utf-8 -*-
from django.db import models
#from django.forms import ModelForm
from django import forms
from models import *
from foros.models import *
from ckeditor.widgets import CKEditorWidget

class AgendaForm(forms.ModelForm):
    descripcion = forms.CharField(widget=CKEditorWidget())

    class Meta:
    	model = Agendas
    	exclude = ('user',)

class DocuForm(forms.ModelForm):
    class Meta:
    	model = Documentos
    	exclude = ('content_type', 'object_id', 'content_object',)