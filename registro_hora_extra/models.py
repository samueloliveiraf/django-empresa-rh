from django.db import models
from funcionarios.models import Funcionario
from django.urls import reverse


class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    hora = models.DecimalField(max_digits=5, decimal_places=2)

    def get_absolute_url(self):
        return reverse('list_hora_extra')


    def __str__(self):
        return self.motivo
