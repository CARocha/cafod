# -*- coding: UTF-8 -*-

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pais(models.Model):
    nombre = models.CharField(max_length=200)
    latitud = models.FloatField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Paises"

    def __unicode__(self):
        return self.nombre

class Contraparte(models.Model):
    nombre = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="logos/", blank=True, null=True)
    pais = models.ForeignKey(Pais)
    fundacion = models.CharField('Año de fundacion', max_length=200, 
                                 blank=True, null=True)
    temas = models.TextField(blank=True, null=True)
    generalidades = models.TextField(blank=True, null=True)
    contacto = models.CharField(max_length=200,blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)
    sitio_web = models.URLField(blank=True, null=True)
    rss = models.CharField(max_length=200,blank=True, null=True)
    user = models.ForeignKey(User)

    class Meta:
        verbose_name_plural = "Contrapartes"

    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        return '/contrapartes/%d/' % (self.id,)

#class Usuarios(User):
    #usuario = models.ForeignKey(User, related_name="usuario")
    #contraparte = models.ForeignKey(Contraparte)

    #class Meta:
        #verbose_name_plural = "Usuarios"

    #def __unicode__(self):
    #    return u"%s - %s" % (self.usuario.username, self.contraparte.nombre)
class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)
    # Other fields here
    contraparte = models.ForeignKey(Contraparte)