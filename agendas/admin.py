from django.contrib import admin
from models import *

class DocumentosInline(generic.GenericTabularInline):
    model = Documentos
    extra = 1

class AgendasAdmin(admin.ModelAdmin):
    inlines = [DocumentosInline,]
    class Media:
        js = ['../files/js/tiny_mce/tiny_mce.js',
              '../files/js/editores/textareas.js',]




admin.site.register(Agendas, AgendasAdmin)