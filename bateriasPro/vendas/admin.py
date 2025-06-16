# vendas/admin.py
from django.contrib import admin, messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Venda, ItemVenda, Carro
from .service import VendaService
from django.db import transaction
from .repository import ItemVendaRepository

class ItemVendaInline(admin.TabularInline):
    model = ItemVenda
    extra = 1

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    pass

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    inlines = [ItemVendaInline]
    list_display = ['id', 'cliente', 'carro', 'data', 'sucata_recebida_kg', 'desconto_por_sucata']

    def response_add(self, request, obj, post_url_continue=None):
        if getattr(self, "_erro_estoque", False):
            add_url = reverse('admin:vendas_venda_add')
            return HttpResponseRedirect(add_url)
        return super().response_add(request, obj, post_url_continue)

    def save_related(self, request, form, formsets, change):
        try:
            with transaction.atomic():
                super().save_related(request, form, formsets, change)

                venda = form.instance
                itens = ItemVendaRepository.get_by_venda(venda)
                VendaService.processar_venda(venda, itens)

        except ValueError as e:
            self.message_user(request, str(e), level=messages.ERROR)
            form.instance.delete()
            self._erro_estoque = True
