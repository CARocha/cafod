# -*- coding: UTF-8 -*-

from django.db import models
from django.contrib.contenttypes import generic
from contrapartes.models import *
from foros.models import *
from django.template.defaultfilters import slugify

# Create your models here.

class Notas(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    fecha = models.DateField('Fecha de publicación', default=datetime.datetime.now())
    contenido = models.TextField()
    fotos = generic.GenericRelation(Imagen)
    adjuntos = generic.GenericRelation(Documentos)

    user = models.ForeignKey(User)

    class Meta:
    	verbose_name_plural = "Notas"

    def __unicode__(self):
    	return self.titulo

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.titulo)
        return super(Notas, self).save(*args, **kwargs)

    def imagenes(self):
        imagenes = Imagen.objects.filter(object_id=self.id)
        return imagenes

    def adjunto(self):
        adjunto = Documentos.objects.filter(object_id=self.id)
        return adjunto

    def get_absolute_url(self):
    	return '/notas/%d/' % (self.id,)