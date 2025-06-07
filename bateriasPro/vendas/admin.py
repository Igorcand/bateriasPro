# vendas/admin.py
from django.contrib import admin
from .models import Venda, ItemVenda, Carro
from estoque.models import Bateria
from sucata.models import MovimentacaoSucata, TipoMovimentacao
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db import transaction
from django.utils.translation import gettext_lazy as _

class ItemVendaInline(admin.TabularInline):
    model = ItemVenda
    extra = 1

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    inlines = [ItemVendaInline]
    list_display = ['id', 'cliente', 'carro', 'data', 'sucata_recebida_kg', 'desconto_por_sucata']

    def response_add(self, request, obj, post_url_continue=None):
        if getattr(self, "_erro_estoque", False):
            # Retorna para a mesma página sem a mensagem de sucesso
            from django.urls import reverse
            add_url = reverse('admin:vendas_venda_add')
            return HttpResponseRedirect(add_url)

        return super().response_add(request, obj, post_url_continue)
    
    def save_related(self, request, form, formsets, change):
        obj = form.instance

        try:
            with transaction.atomic():
                super().save_related(request, form, formsets, change)

                itens = ItemVenda.objects.filter(venda=obj)

                # Verifica se todos os itens têm estoque suficiente
                for item in itens:
                    if item.quantidade > item.bateria.quantidade_em_estoque:
                        raise ValueError(
                            f"Estoque insuficiente para Bateria '{item.bateria.marca}'. "
                            f"Disponível: {item.bateria.quantidade_em_estoque}, Solicitado: {item.quantidade}"
                        )

                # Se passou, subtrai o estoque
                for item in itens:
                    bateria = item.bateria
                    bateria.quantidade_em_estoque -= item.quantidade
                    bateria.save()
                
                # Adiciona movimentação de sucata se houver sucata recebida
                if obj.sucata_recebida_kg and obj.sucata_recebida_kg > 0:
                    MovimentacaoSucata.objects.create(
                        tipo=TipoMovimentacao.ENTRADA_TROCA,
                        quantidade_kg=obj.sucata_recebida_kg,
                        venda=obj,
                        observacao=f"Recebida via venda #{obj.id}"
                    )

        except ValueError as e:
            self.message_user(request, str(e), level=messages.ERROR)

            # Remove a venda salva anteriormente (rollback manual)
            obj.delete()
            self._erro_estoque = True  # marca que deu erro

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ['placa', 'modelo', 'ano', 'cliente']
