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