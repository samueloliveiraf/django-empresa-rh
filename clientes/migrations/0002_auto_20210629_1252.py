# Generated by Django 3.2.4 on 2021-06-29 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='cep',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='numero',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='rua',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
