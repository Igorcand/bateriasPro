from django.db import models
from vendas.models import Venda

class TipoMovimentacao(models.TextChoices):
    ENTRADA_TROCA = 'entrada_troca', 'Entrada (Troca na venda)'
    ENTRADA_COMPRA = 'entrada_compra', 'Entrada (Compra avulsa)'
    SAIDA_VENDA = 'saida_venda', 'Saída (Venda por fora)'
    SAIDA_DISTRIBUIDORA = 'saida_distribuidora', 'Saída (Enviada para distribuidora)'

class MovimentacaoSucata(models.Model):
    tipo = models.CharField(max_length=30, choices=TipoMovimentacao.choices)
    quantidade_kg = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField(auto_now_add=True)
    observacao = models.TextField(blank=True, null=True)

    venda = models.ForeignKey(
        Venda,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='movimentacoes_sucata'
    )

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.quantidade_kg} kg em {self.data}"

    @classmethod
    def saldo_sucata(cls):
        entradas = cls.objects.filter(tipo__startswith='entrada').aggregate(models.Sum('quantidade_kg'))['quantidade_kg__sum'] or 0
        saidas = cls.objects.filter(tipo__startswith='saida').aggregate(models.Sum('quantidade_kg'))['quantidade_kg__sum'] or 0
        return entradas - saidas

class EstoqueSucata(models.Model):
    quantidade_kg = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Estoque atual de sucata: {self.quantidade_kg} kg"