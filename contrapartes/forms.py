# -*- coding: UTF-8 -*-
from django.db import models
from django.forms import ModelForm
from models import *
from django import forms
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.models import User

class ContraparteForms(forms.ModelForm):
	temas = forms.CharField(widget=CKEditorWidget())
	generalidades = forms.CharField(widget=CKEditorWidget())
	nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'span7','rel':"tooltip", 'title':"Nombre Completo de la Contraparte"}))
	fundacion = forms.CharField(widget=forms.TextInput(attrs={'rel':"tooltip", 'title':"Año en que fue fundada la organización"}))
	contacto = forms.CharField(required=False,widget=forms.TextInput(attrs={'rel':"tooltip", 'title':"Nombre completo de la persona de contacto"}))
	telefono = forms.IntegerField(required=False,widget=forms.TextInput(attrs={'rel':"tooltip", 'title':"Formato ### - ######## "}))
	sitio_web = forms.URLField(required=False,widget=forms.TextInput(attrs={'rel':"tooltip", 'title':"con este formato http://www.dominio.com "}))
	rss = forms.CharField(required=False,widget=forms.TextInput(attrs={'rel':"tooltip", 'title':"Direccion rss de contenido sindicado"}))
    
	class Meta:
		model = Contraparte
		exclude = ('user',)

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')

class UserProfileForm(ModelForm):
	class Meta:
		model = UserProfile
		fields = ('avatar',)

