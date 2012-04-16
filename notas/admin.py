from django.contrib import admin
from models import *
from foros.models import *

class DocumentosInline(generic.GenericTabularInline):
    model = Documentos
    extra = 1

class ImagenInline(generic.GenericTabularInline):
    model = Imagen
    extra = 1

class NotasAdmin(admin.ModelAdmin):
    class Media:
        js = ['../files/js/tiny_mce/tiny_mce.js',
              '../files/js/editores/textareas.js',]
    #class Media:
    #	css = {
    #	    "all": ("css/custom.css",)
    #	}

    inlines = [ImagenInline, DocumentosInline, ]


admin.site.register(Notas, NotasAdmin)