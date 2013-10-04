from django.contrib import admin
from models import *
from foros.models import *
from foros.forms import *

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
    form = ForosForm
    list_display = ['nombre','creacion','contraparte',
                    '__documento__','__fotos__', '__video__',
                    '__audio__']
    date_hierarchy = 'creacion'

class AportesAdmin(admin.ModelAdmin):
    inlines = [DocumentosInline, ImagenInline, 
              VideosInline, AudiosInline]
    form = AporteForm
    list_display = ['__unicode__','fecha','user',
                    '__documento__','__fotos__', 
                    '__video__','__audio__']
    list_filter = ['user','fecha']
    date_hierarchy = 'fecha'

class ComentariosAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'usuario', 'aporte')
    form = ComentarioForm

admin.site.register(Foros, ForoAdmin)
admin.site.register(Aportes, AportesAdmin)
admin.site.register(Comentarios, ComentariosAdmin)
admin.site.register(Documentos)
admin.site.register(Imagen)
admin.site.register(Videos)
admin.site.register(Audios)