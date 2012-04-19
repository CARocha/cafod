from django.db import models
from django.forms import ModelForm
from models import *
from django import forms
from ckeditor.widgets import CKEditorWidget

class ContraparteForms(forms.ModelForm):
    temas = forms.CharField(widget=CKEditorWidget())
    generalidades = forms.CharField(widget=CKEditorWidget())

    class Meta:
    	model = Contraparte
    	exclude = ('user',)