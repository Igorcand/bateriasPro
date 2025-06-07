from .models import ItemVenda
from estoque.models import Bateria

class ItemVendaRepository:
    @staticmethod
    def get_by_venda(venda):
        return ItemVenda.objects.filter(venda=venda)

class BateriaRepository:
    @staticmethod
    def atualizar_estoque(bateria, quantidade):
        bateria.quantidade_em_estoque -= quantidade
        bateria.save()
