from django.db import models
from django.forms import ModelForm
from models import *

class ForosForm(ModelForm):
    class Meta:
    	model = Foros
    	exclude = ('contraparte','creacion',)

class AporteForm(ModelForm):
    class Meta:
    	model = Aportes
    	exclude = ('foro','fecha','user',)

class ComentarioForm(ModelForm):
    class Meta:
    	model = Comentarios
    	exclude = ('fecha','aporte','usuario')

class ImagenForm(ModelForm):
    class Meta:
    	model = Imagen
    	exclude = ('content_type', 'object_id', 'content_object',)

class DocumentoForm(ModelForm):
    class Meta:
    	model = Documentos
    	exclude = ('content_type', 'object_id', 'content_object',)

class VideoForm(ModelForm):
    class Meta:
    	model = Videos
    	exclude = ('content_type', 'object_id', 'content_object',)

class AudioForm(ModelForm):
    class Meta:
    	model = Audios
    	exclude = ('content_type', 'object_id', 'content_object',)
