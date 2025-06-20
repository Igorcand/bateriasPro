# Generated by Django 5.2.1 on 2025-05-25 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bateria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('amperagem', models.PositiveIntegerField(help_text='Em Ah')),
                ('peso_kg', models.DecimalField(decimal_places=2, max_digits=5)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantidade_em_estoque', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Sucata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade_kg', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
