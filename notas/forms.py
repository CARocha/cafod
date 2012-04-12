from django.db import models
from django.forms import ModelForm
from models import *
from foros.models import *

class NotasForms(ModelForm):
    class Meta:
    	model = Notas
    	exclude = ('slug','fecha','user',)

class FotoForm(ModelForm):
	class Meta:
		model = Imagen
		exclude = ('content_type', 'object_id', 'content_object',)

class AdjuntoForm(ModelForm):
	class Meta:
		model = Documentos
		exclude = ('content_type', 'object_id', 'content_object',)
