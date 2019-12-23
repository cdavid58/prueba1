from django.contrib import admin
from .models import *

class ServiciosAdmin(admin.ModelAdmin):
	list_display = ('nombre',)

admin.site.register(Servicios,ServiciosAdmin)
admin.site.register(ImgCarrucel)
admin.site.register(diseñoGeneral)
