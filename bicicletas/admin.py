from django.contrib import admin

from .models import Estado, Repuesto
# Register your models here.

class EstadoAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'updated_at')

admin.site.register(Estado, EstadoAdmin)

class RepuestoAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'updated_at')

admin.site.register(Repuesto, RepuestoAdmin)

#configurar el titulo del panel
title = "Inventario de Bicicletas"
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = "Panel de gestion"

