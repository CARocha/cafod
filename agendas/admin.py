from django.contrib import admin
from models import *
from ckeditor.widgets import CKEditorWidget
from agendas.forms import *
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
from django.contrib.flatpages.admin import FlatpageForm as FlatpageFormOld
 
from django import forms
from ckeditor.widgets import CKEditorWidget
 
class FlatpageForm(FlatpageFormOld):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = FlatPage
 
 
class FlatPageAdmin(FlatPageAdminOld):
    form = FlatpageForm
 
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)

class DocumentosInline(generic.GenericTabularInline):
    model = Documentos
    extra = 1

class AgendasAdmin(admin.ModelAdmin):
    inlines = [DocumentosInline,]
    form = AgendaForm
    #class Media:
    #    js = ['../files/js/tiny_mce/tiny_mce.js',
    #          '../files/js/editores/textareas.js',]




admin.site.register(Agendas, AgendasAdmin)