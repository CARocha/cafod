# -*- coding: UTF-8 -*-

from django.db import models
from foros.models import Documentos
from django.contrib.contenttypes import generic
from django.contrib.auth.models import User

# Create your models here.

class Agendas(models.Model):
    evento = models.CharField(max_length=200)
    descripcion = models.TextField('Descripción')
    inicio = models.DateField('Fecha de Inicio')
    final = models.DateField('Fecha de Finalización')
    publico = models.BooleanField()
    adjunto = generic.GenericRelation(Documentos)
    user = models.ForeignKey(User)

    class Meta:
    	verbose_name_plural = "Agendas"

    def __unicode__(self):
    	return self.evento

    def get_absolute_url(self):
        return '/agendas/%d/' % (self.id,)


