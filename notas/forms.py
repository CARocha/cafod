from django.db import models
from django.forms import ModelForm
from models import *

class NotasForms(ModelForm):
    class Meta:
    	model = Notas
    	exclude = ('slug','fecha','user',)