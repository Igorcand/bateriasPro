from django.contrib import admin
from .models import PendenciaFinanceira, Financeiro

@admin.register(PendenciaFinanceira)
class PendenciaFinanceiraAdmin(admin.ModelAdmin):
    list_display = ['fornecedor', 'valor', 'prazo_pagamento', 'sucata_prometida_kg']

@admin.register(Financeiro)
class FinanceiroAdmin(admin.ModelAdmin):
    list_display = ['id', 'tipo', 'valor', 'data', 'venda', 'pendencia']
    list_filter = ['tipo', 'data']
