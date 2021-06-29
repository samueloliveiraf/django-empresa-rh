from django.db import models
from empresas.models import Empresa
from cpf_field.models import CPFField
from django.urls import reverse


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = CPFField('cpf')
    empresa = models.ForeignKey(
    Empresa, on_delete=models.PROTECT, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('list_clientes')

    def __str__(self):
        return self.nome
