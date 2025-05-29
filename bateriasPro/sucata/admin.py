from django.contrib import admin
from .models import MovimentacaoSucata, EstoqueSucata

@admin.register(MovimentacaoSucata)
class MovimentacaoSucataAdmin(admin.ModelAdmin):
    list_display = ['tipo', 'quantidade_kg', 'data']
    list_filter = ['tipo', 'data']
    search_fields = ['observacao']

@admin.register(EstoqueSucata)
class EstoqueSucataAdmin(admin.ModelAdmin):
    list_display = ['quantidade_kg']