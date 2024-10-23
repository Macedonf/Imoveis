# Generated by Django 5.1.2 on 2024-10-23 16:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco', models.CharField(max_length=255)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=2)),
                ('preco_aluguel', models.DecimalField(decimal_places=2, max_digits=8)),
                ('descricao', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inquilino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('Imovel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imoveis.imovel')),
            ],
        ),
        migrations.CreateModel(
            name='Aluguel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_vencimento', models.DateField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=8)),
                ('pago', models.BooleanField(default=False)),
                ('inquilino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imoveis.inquilino')),
            ],
        ),
    ]
