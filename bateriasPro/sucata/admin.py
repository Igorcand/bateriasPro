from django.contrib import admin
from .models import MovimentacaoSucata

@admin.register(MovimentacaoSucata)
class MovimentacaoSucataAdmin(admin.ModelAdmin):
    list_display = ['tipo', 'quantidade_kg', 'data']
    list_filter = ['tipo', 'data']
    search_fields = ['observacao']
