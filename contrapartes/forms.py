from django.db import models
from django.forms import ModelForm
from models import *
#from django.contrib.admin.widgets import AdminFileWidget
#from django import forms

class ContraparteForms(ModelForm):
    #logo = forms.FileField(widget=AdminFileWidget)
    class Meta:
    	model = Contraparte
    	exclude = ('user',)