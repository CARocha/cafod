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
    	css = {
    	    "all": ("css/custom.css",)
    	}
    prepopulated_fields = { 'slug': ['titulo']}
    inlines = [DocumentosInline, ImagenInline]


admin.site.register(Notas, NotasAdmin)