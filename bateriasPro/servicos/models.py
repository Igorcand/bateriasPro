from django.db import models

class TipoServico(models.TextChoices):
    INSTALACAO = "INSTALACAO", "Instalação"
    TESTE = "TESTE", "Teste de bateria"
    LIMPEZA = "LIMPEZA", "Limpeza de polo"
    CARGA = "CARGA", "Carga de bateria"
    OUTRO = "OUTRO", "Outro"

class Servico(models.Model):
    tipo = models.CharField(max_length=20, choices=TipoServico.choices)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.get_tipo_display()} - R$ {self.preco}"
