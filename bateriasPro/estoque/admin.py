from django.contrib import admin
from .models import Bateria, Marca

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']

@admin.register(Bateria)
class BateriaAdmin(admin.ModelAdmin):
    list_display = ['marca', 'modelo', 'amperagem', 'peso_kg', 'quantidade_em_estoque']
    search_fields = ['modelo']