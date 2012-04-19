# -*- coding: UTF-8 -*-

from django.db import models
#from django.forms import ModelForm
from tagging.forms import TagField
from tagging_autocomplete.widgets import TagAutocomplete
from models import *
from django import forms
from ckeditor.widgets import CKEditorWidget


class ForosForm(forms.ModelForm):
    contenido = forms.CharField(widget=CKEditorWidget())
    class Meta:
    	model = Foros
    	exclude = ('contraparte','creacion',)

class AporteForm(forms.ModelForm):
    contenido = forms.CharField(widget=CKEditorWidget())
    class Meta:
    	model = Aportes
    	exclude = ('foro','fecha','user',)

class ComentarioForm(forms.ModelForm):
    comentario = forms.CharField(widget=CKEditorWidget())
    class Meta:
    	model = Comentarios
    	exclude = ('fecha','aporte','usuario')

class ImagenForm(forms.ModelForm):
    tags_img = TagField(widget=TagAutocomplete(), required=False)

    class Meta:
    	model = Imagen
    	exclude = ('content_type', 'object_id', 'content_object',)

class DocumentoForm(forms.ModelForm):
    tags_doc = TagField(widget=TagAutocomplete(), required=False)

    class Meta:
    	model = Documentos
    	exclude = ('content_type', 'object_id', 'content_object',)

class VideoForm(forms.ModelForm):
    tags_vid = TagField(widget=TagAutocomplete(), required=False)

    class Meta:
    	model = Videos
    	exclude = ('content_type', 'object_id', 'content_object',)

class AudioForm(forms.ModelForm):
    tags_aud = TagField(widget=TagAutocomplete(), required=False)

    class Meta:
    	model = Audios
    	exclude = ('content_type', 'object_id', 'content_object',)
