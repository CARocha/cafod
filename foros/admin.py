from django.contrib import admin
from models import *
from foros.models import *

class DocumentosInline(generic.GenericTabularInline):
    model = Documentos
    extra = 1

class ImagenInline(generic.GenericTabularInline):
    model = Imagen
    extra = 1

class VideosInline(generic.GenericTabularInline):
    model = Videos
    extra = 1

class AudiosInline(generic.GenericTabularInline):
    model = Audios
    extra = 1

class ForoAdmin(admin.ModelAdmin):
    inlines = [DocumentosInline, ImagenInline, 
              VideosInline, AudiosInline]

class AportesAdmin(admin.ModelAdmin):
	inlines = [DocumentosInline, ImagenInline, 
              VideosInline, AudiosInline]

admin.site.register(Foros, ForoAdmin)
admin.site.register(Aportes, AportesAdmin)
admin.site.register(Cometarios)