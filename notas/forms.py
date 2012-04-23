from django.db import models
#from django.forms import ModelForm
from models import *
from foros.models import *
from django import forms
from ckeditor.widgets import CKEditorWidget

class NotasForms(forms.ModelForm):
    contenido = forms.CharField(widget=CKEditorWidget())
    titulo = forms.CharField(widget=forms.TextInput(attrs={'class':'span7','rel':"tooltip", 'title':"Tratar de redactar titulos resumidos"}))
    class Meta:
    	model = Notas
    	exclude = ('slug','fecha','user',)

class FotoForm(forms.ModelForm):
	class Meta:
	    model = Imagen
	    exclude = ('content_type', 'object_id', 'content_object',)

class AdjuntoForm(forms.ModelForm):
	class Meta:
	    model = Documentos
	    exclude = ('content_type', 'object_id', 'content_object',)
