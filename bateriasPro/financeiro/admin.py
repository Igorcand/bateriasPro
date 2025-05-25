from django.contrib import admin
from .models import PendenciaFinanceira

@admin.register(PendenciaFinanceira)
class PendenciaFinanceiraAdmin(admin.ModelAdmin):
    list_display = ['fornecedor', 'valor', 'prazo_pagamento', 'sucata_prometida_kg']
