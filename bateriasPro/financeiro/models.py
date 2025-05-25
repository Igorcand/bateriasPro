from django.db import models
from fornecedores.models import Fornecedor

class PendenciaFinanceira(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_registro = models.DateField(auto_now_add=True)
    prazo_pagamento = models.DateField()
    sucata_prometida_kg = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.fornecedor} - R$ {self.valor} até {self.prazo_pagamento}"
