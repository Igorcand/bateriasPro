from django.db import models
from clientes.models import Cliente
from estoque.models import Bateria

class Manutencao(models.Model):
    STATUS_CHOICES = [
        ('analise', 'Em análise'),
        ('defeito', 'Defeito'),
        ('troca', 'Troca fornecedor'),
        ('ok', 'Sem defeito'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='baterias')
    bateria = models.ForeignKey(Bateria, on_delete=models.CASCADE, related_name='manutencoes', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='analise')
    data_entrada = models.DateField(auto_now_add=True)
    data_saida = models.DateField(blank=True, null=True)
    codigo_unico = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"Bateria {self.codigo_unico} - {self.cliente.nome}"
