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
from south.modelsinspector import add_introspection_rules
from ckeditor.fields import RichTextField

add_introspection_rules ([], ["^ckeditor\.fields\.RichTextField"])
add_introspection_rules ([], ["^tagging_autocomplete\.models\.TagAutocompleteField"])

# Create your models here.

class Imagen(models.Model):
    ''' Modelo generico para subir imagenes en todos los demas app :)'''
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    nombre_img = models.CharField("Nombre",max_length=200, null=True, blank=True)
    foto = ImageWithThumbsField("Foto",upload_to=get_file_path,
                                   sizes=((220,160), (80,80),(380,250),(640,480)), 
                                   null=True, blank=True)
    tags_img = TagAutocompleteField("Tags",help_text='Separar elementos con "," ', null=True, blank=True)
    fileDir = 'fotos/'
    class Meta:
    	verbose_name_plural = "Imágenes"

    def __unicode__(self):
    	return self.nombre_img

class Documentos(models.Model):
    ''' Modelo generico para subir los documentos en distintos app'''
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    nombre_doc = models.CharField("Nombre",max_length=200, null=True, blank=True)
    adjunto = models.FileField("Adjunto",upload_to=get_file_path, null=True, blank=True)
    tags_doc = TagAutocompleteField("Tags",help_text='Separar elementos con "," ', null=True, blank=True)

    fileDir = 'documentos/'

    class Meta:
    	verbose_name_plural = "Documentos"

    def __unicode__(self):
    	return self.nombre_doc

class Videos(models.Model):
    ''' Modelo generico para subir videos en todos los app'''
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    nombre_video = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    tags_vid = TagAutocompleteField(help_text='Separar elementos con "," ', null=True, blank=True)

    class Meta:
    	verbose_name_plural = "Videos"

    def __unicode__(self):
    	return self.nombre_video

class Audios(models.Model):
    '''' Modelo generico para subir audios en todos los demas app '''
    content_type = models.ForeignKey(ContentType)
    object_id = models.IntegerField(db_index=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    nombre_audio = models.CharField(max_length=200, null=True, blank=True)
    audio = models.FileField(upload_to=get_file_path, null=True, blank=True)
    tags_aud = TagAutocompleteField(help_text='Separar elementos con "," ', null=True, blank=True)

    fileDir = 'audios/'

    class Meta:
    	verbose_name_plural = "Audios"

    def __unicode__(self):
    	return self.nombre_audio

class Foros(models.Model):
    nombre = models.CharField(max_length=200)
    creacion = models.DateField(default=datetime.datetime.now())
    apertura = models.DateField('Apertura y recepción de aportes')
    cierre = models.DateField('Cierre de aportes')
    fecha_skype = models.DateField('Propuesta de reunión skype')
    memoria = models.DateField('Propuesta entrega de memoria')
    contenido = RichTextField()
    contraparte = models.ForeignKey(User)
    documentos = generic.GenericRelation(Documentos)
    fotos = generic.GenericRelation(Imagen)
    video = generic.GenericRelation(Videos)
    audio = generic.GenericRelation(Audios)

    class Meta:
    	verbose_name_plural = "Foros"
        ordering = ['-creacion']

    def __unicode__(self):
    	return self.nombre

    def get_absolute_url(self):
        return "/foros/ver/%d" % (self.id)

class Aportes(models.Model):
    foro = models.ForeignKey(Foros)
    fecha = models.DateField(default=datetime.datetime.now())
    contenido = RichTextField()
    user = models.ForeignKey(User)
    adjuntos = generic.GenericRelation(Documentos)
    fotos = generic.GenericRelation(Imagen)
    video = generic.GenericRelation(Videos)
    audio = generic.GenericRelation(Audios)

    class Meta:
        verbose_name_plural = "Aportes"

    def __unicode__(self):
        return self.foro.nombre

class Comentarios(models.Model):
    fecha = models.DateField(default=datetime.datetime.now())
    usuario = models.ForeignKey(User)
    comentario = RichTextField()
    aporte = models.ForeignKey(Aportes)

    class Meta:
        verbose_name_plural = "Comentarios"

    def __unicode__(self):
        return self.usuario.username
