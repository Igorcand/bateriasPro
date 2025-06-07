from django.db import models
from fornecedores.models import Fornecedor
from vendas.models import Venda

class PendenciaFinanceira(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_registro = models.DateField(auto_now_add=True)
    prazo_pagamento = models.DateField()
    sucata_prometida_kg = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.fornecedor} - R$ {self.valor} até {self.prazo_pagamento}"


class TipoFinanceiro(models.TextChoices):
    ENTRADA = 'ENTRADA', 'Entrada'
    SAIDA = 'SAIDA', 'Saída'

class Financeiro(models.Model):
    tipo = models.CharField(max_length=10, choices=TipoFinanceiro.choices)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField(auto_now_add=True)
    descricao = models.TextField(blank=True)

    venda = models.ForeignKey(
        Venda,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='financeiros'
    )

    # Relacionamento opcional com pendência
    pendencia = models.ForeignKey(
        PendenciaFinanceira,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='financeiros'
    )

    def __str__(self):
        return f"{self.tipo} - R$ {self.valor} em {self.data}"