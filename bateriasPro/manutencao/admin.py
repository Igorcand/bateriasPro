from django.contrib import admin
from .models import Manutencao

@admin.register(Manutencao)
class ManutencaoAdmin(admin.ModelAdmin):
    list_display = ('codigo_unico', 'cliente', 'status', 'data_entrada', 'data_saida')
    search_fields = ('codigo_unico', 'cliente__nome')
    list_filter = ('status', 'data_entrada', 'data_saida')
