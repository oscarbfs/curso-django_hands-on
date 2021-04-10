from django.contrib import admin

from pypro.canais.models import Canal


@admin.register(Canal)
class CanalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug', 'inicio', 'fim')
    prepopulated_fields = {'slug': ('nome',)}
    ordering = ('-inicio',)
