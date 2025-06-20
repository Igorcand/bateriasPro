# Generated by Django 5.2.1 on 2025-05-25 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovimentacaoSucata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('entrada_troca', 'Entrada (Troca na venda)'), ('entrada_compra', 'Entrada (Compra avulsa)'), ('saida_venda', 'Saída (Venda por fora)'), ('saida_distribuidora', 'Saída (Enviada para distribuidora)')], max_length=30)),
                ('quantidade_kg', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data', models.DateField(auto_now_add=True)),
                ('observacao', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
