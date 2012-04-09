from django.contrib import admin
from models import *

class DocumentosInline(generic.GenericTabularInline):
    model = Documentos
    extra = 1

class AgendasAdmin(admin.ModelAdmin):
	inlines = [DocumentosInline,]



admin.site.register(Agendas, AgendasAdmin)