from django.db import models
from django.contrib.auth.models import User
from departamentos.models import Departamento
from empresas.models import Empresa
from django.urls import reverse
from django.db.models import Sum


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True)

    @property
    def total_horas_extra(self):
        total = self.registrohoraextra_set.all().aggregate(
            Sum('hora'))['hora__sum']
        return total or 0

    def get_absolute_url(self):
        return reverse('list_funcionarios')

    def __str__(self):
        return self.nome
