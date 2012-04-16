from django.contrib import admin
from models import *

class ContraparteAdmin(admin.ModelAdmin):
    class Media:
        js = ['../files/js/tiny_mce/tiny_mce.js',
              '../files/js/editores/textareas.js',]

admin.site.register(Pais)
admin.site.register(Contraparte, ContraparteAdmin)
admin.site.register(UserProfile)