from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome

class Bateria(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=50)
    amperagem = models.PositiveIntegerField(help_text="Em Ah")
    peso_kg = models.DecimalField(max_digits=5, decimal_places=2)
    quantidade_em_estoque = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.marca} {self.modelo} {self.amperagem}Ah"
