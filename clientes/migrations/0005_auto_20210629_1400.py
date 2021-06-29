# Generated by Django 3.2.4 on 2021-06-29 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_merge_0002_cliente_cep_0003_alter_cliente_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cep',
            field=models.DecimalField(decimal_places=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='numero',
            field=models.CharField(max_length=15),
        ),
    ]
