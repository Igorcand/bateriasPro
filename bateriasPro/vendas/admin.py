# vendas/admin.py
from django.contrib import admin, messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Venda, ItemVenda, Carro
from .service import VendaService

class ItemVendaInline(admin.TabularInline):
    model = ItemVenda
    extra = 1

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
        obj = form.instance

        try:
            super().save_related(request, form, formsets, change)
            VendaService.processar_venda(obj)

        except ValueError as e:
            self.message_user(request, str(e), level=messages.ERROR)
            obj.delete()
            self._erro_estoque = True
