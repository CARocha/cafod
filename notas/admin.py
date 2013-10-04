from django.contrib import admin
from models import *
from foros.models import *
from notas.forms import NotasForms

class DocumentosInline(generic.GenericTabularInline):
    model = Documentos
    extra = 1

class ImagenInline(generic.GenericTabularInline):
    model = Imagen
    extra = 1

class NotasAdmin(admin.ModelAdmin):
    form = NotasForms
    #class Media:
    #	css = {
    #	    "all": ("css/custom.css",)
    #	}

    inlines = [ImagenInline, DocumentosInline, ]
    list_display = ['__unicode__','fecha','user']
    list_filter = ['user','fecha']
    date_hierarchy = 'fecha'


admin.site.register(Notas, NotasAdmin)