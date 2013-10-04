from django.contrib import admin
from models import *
from ckeditor.widgets import CKEditorWidget
from contrapartes.forms import *

class ContraparteAdmin(admin.ModelAdmin):
	form = ContraparteForms
    #class Media:
    #    js = ['../files/js/tiny_mce/tiny_mce.js',
    #          '../files/js/editores/textareas.js',]

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['__unicode__','__fecha_registro__']

admin.site.register(Pais)
admin.site.register(Contraparte, ContraparteAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Mensajero)