# Generated by Django 3.2.4 on 2021-06-29 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0003_alter_funcionario_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='salario',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=6),
            preserve_default=False,
        ),
    ]
