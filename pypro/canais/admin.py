from django.contrib import admin

from pypro.canais.models import Canal


class InscricaoInline(admin.TabularInline):
    model = Canal.usuarios.through
    extra = 1
    readonly_fields = ('data',)
    autocomplete_fields = ('usuario',)
    ordering = ('-data',)


@admin.register(Canal)
class CanalAdmin(admin.ModelAdmin):
    inlines = [InscricaoInline]
    list_display = ('nome', 'slug', 'inicio', 'fim')
    prepopulated_fields = {'slug': ('nome',)}
    ordering = ('-inicio',)
