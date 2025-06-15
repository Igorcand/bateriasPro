from .repository import VendaRepository, ItemVendaRepository, BateriaRepository
from sucata.models import MovimentacaoSucata, TipoMovimentacao
from django.db import transaction

class VendaService:
    @staticmethod
    def processar_venda(venda, itens=None):
        if itens is None:
            itens = ItemVendaRepository.get_by_venda(venda)

        for item in itens:
            if item.quantidade > item.bateria.quantidade_em_estoque:
                raise ValueError(
                    f"Estoque insuficiente para Bateria '{item.bateria.marca}'. "
                    f"Disponível: {item.bateria.quantidade_em_estoque}, Solicitado: {item.quantidade}"
                )

        for item in itens:
            BateriaRepository.atualizar_estoque(item.bateria, item.quantidade)

        if venda.sucata_recebida_kg and venda.sucata_recebida_kg > 0:
            MovimentacaoSucata.objects.create(
                tipo=TipoMovimentacao.ENTRADA_TROCA,
                quantidade_kg=venda.sucata_recebida_kg,
                venda=venda,
                observacao=f"Recebida via venda #{venda.id}"
            )
