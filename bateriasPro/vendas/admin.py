from django.contrib import admin
from .models import Venda, ItemVenda, Carro

class ItemVendaInline(admin.TabularInline):
    model = ItemVenda
    extra = 1

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    inlines = [ItemVendaInline]
    list_display = ['cliente', 'carro', 'data', 'sucata_recebida_kg', 'desconto_por_sucata', 'total']
    readonly_fields = ['total']
    filter_horizontal = ['servicos']

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ['placa', 'modelo', 'ano', 'cliente']
    search_fields = ['placa', 'modelo']