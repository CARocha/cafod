# -*- coding: UTF-8 -*-

from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from south.modelsinspector import add_introspection_rules
from tagging.models import Tag
from tagging_autocomplete.models import TagAutocompleteField
from django.contrib.auth.models import User
#from contrapartes.models import Usuarios
from thumbs import ImageWithThumbsField
from utils import *
import datetime

add_introspection_rules ([], ["^tagging_autocomplete\.models\.TagAutocompleteField"])

# Create your models here.

class Imagen(models.Model):
    ''' Modelo generico para subir imagenes en todos los demas app :)'''
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    nombre = models.CharField(max_length=200)
    foto = ImageWithThumbsField(upload_to=get_file_path,
                                   sizes=((350,250), (132,117)), 
                                   null=True, blank=True)
    tags = TagAutocompleteField(help_text='Separar elementos con "," ')
    fileDir = 'fotos/'
    class Meta:
    	verbose_name_plural = "Imagenes"

    def __unicode__(self):
    	return self.nombre

class Documentos(models.Model):
    ''' Modelo generico para subir los documentos en distintos app'''
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    nombre = models.CharField(max_length=200)
    adjunto = models.FileField(upload_to=get_file_path, null=True, blank=True)
    tags = TagAutocompleteField(help_text='Separar elementos con "," ')

    fileDir = 'documentos/'

    class Meta:
    	verbose_name_plural = "Documentos"

    def __unicode__(self):
    	return self.nombre

class Videos(models.Model):
    ''' Modelo generico para subir videos en todos los app'''
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    nombre = models.CharField(max_length=200)
    url = models.URLField()
    tags = TagAutocompleteField(help_text='Separar elementos con "," ')

    class Meta:
    	verbose_name_plural = "Videos"

    def __unicode__(self):
    	return self.nombre

class Audios(models.Model):
    '''' Modelo generico para subir audios en todos los demas app '''
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    nombre = models.CharField(max_length=200)
    audio = models.FileField(upload_to=get_file_path, null=True, blank=True)
    tags = TagAutocompleteField(help_text='Separar elementos con "," ')

    fileDir = 'audios/'

    class Meta:
    	verbose_name_plural = "Audios"

    def __unicode__(self):
    	return self.nombre

class Foros(models.Model):
    nombre = models.CharField(max_length=200)
    creacion = models.DateField(default=datetime.datetime.now())
    apertura = models.DateField('Apertura y recepción de aporte')
    cierre = models.DateField('Cierre de aportes')
    fecha_skype = models.DateField('Propuesta de reunion skype')
    memoria = models.DateField('Propuesta entrega de memoria')
    contenido = models.TextField()
    contraparte = models.ForeignKey(User)
    documentos = generic.GenericRelation(Documentos)
    fotos = generic.GenericRelation(Imagen)
    video = generic.GenericRelation(Videos)
    audio = generic.GenericRelation(Audios)

    class Meta:
    	verbose_name_plural = "Foros"

    def __unicode__(self):
    	return self.nombre

class Aportes(models.Model):
    foro = models.ForeignKey(Foros)
    fecha = models.DateField()
    contenido = models.TextField()
    user = models.ForeignKey(User)
    documentos = generic.GenericRelation(Documentos)
    fotos = generic.GenericRelation(Imagen)
    video = generic.GenericRelation(Videos)
    audio = generic.GenericRelation(Audios)

    class Meta:
        verbose_name_plural = "Aportes"

    def __unicode__(self):
        return self.foro.nombre

class Cometarios(models.Model):
    fecha = models.DateField()
    usuario = models.ForeignKey(User)
    cometario = models.TextField()
    aporte = models.ForeignKey(Aportes)

    class Meta:
        verbose_name_plural = "Comentarios"

    def __unicode__(self):
        return self.usuario.nombre