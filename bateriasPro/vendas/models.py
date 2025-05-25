from django.db import models
from estoque.models import Bateria
from clientes.models import Cliente
from servicos.models import Servico

class Carro(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    placa = models.CharField(max_length=10, unique=True)
    modelo = models.CharField(max_length=50)
    ano = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.modelo} ({self.placa})"

class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    carro = models.ForeignKey(Carro, on_delete=models.SET_NULL, null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True)
    baterias = models.ManyToManyField(Bateria, through="ItemVenda")
    servicos = models.ManyToManyField(Servico, blank=True)
    sucata_recebida_kg = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    desconto_por_sucata = models.BooleanField(default=False)

    def total(self):
        total = sum(item.preco_unitario * item.quantidade for item in self.itemvenda_set.all())
        total += sum(servico.preco for servico in self.servicos.all())
        if self.desconto_por_sucata and self.sucata_recebida_kg > 0:
            total -= float(self.sucata_recebida_kg) * 2  # Exemplo: 2 reais por kg de sucata
        return round(total, 2)

class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    bateria = models.ForeignKey(Bateria, on_delete=models.CASCADE)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    quantidade = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return round(self.preco_unitario * self.quantidade, 2)
