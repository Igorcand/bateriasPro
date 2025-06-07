from .models import Venda, ItemVenda
from estoque.models import Bateria

class VendaRepository:
    @staticmethod
    def criar(data):
        return Venda.objects.create(**data)

class ItemVendaRepository:
    @staticmethod
    def criar(venda, item_data):
        return ItemVenda.objects.create(venda=venda, **item_data)

    @staticmethod
    def get_by_venda(venda):
        return ItemVenda.objects.filter(venda=venda)

class BateriaRepository:
    @staticmethod
    def atualizar_estoque(bateria, quantidade):
        bateria.quantidade_em_estoque -= quantidade
        bateria.save()
