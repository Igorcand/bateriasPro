from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MovimentacaoSucata, EstoqueSucata, TipoMovimentacao
from vendas.models import Venda

@receiver(post_save, sender=MovimentacaoSucata)
def atualizar_estoque_sucata(sender, instance, **kwargs):
    estoque, created = EstoqueSucata.objects.get_or_create(id=1)
    if instance.tipo == TipoMovimentacao.ENTRADA_TROCA or instance.tipo == TipoMovimentacao.ENTRADA_COMPRA:
        estoque.quantidade_kg += instance.quantidade_kg
    else:  # saída: venda por fora, envio distribuidora etc
        estoque.quantidade_kg -= instance.quantidade_kg

    estoque.quantidade_kg = max(estoque.quantidade_kg, 0)  # evita negativo
    estoque.save()


