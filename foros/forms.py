from django.db import models
from django.forms import ModelForm
from models import *

class ForosForm(ModelForm):
    class Meta:
    	model = Foros
    	exclude = ('contraparte','creacion',)

class AportesForm(ModelForm):
    class Meta:
    	model = Aportes

class CometariosForm(ModelForm):
    class Meta:
    	model = Cometarios