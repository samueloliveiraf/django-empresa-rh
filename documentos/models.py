
from django.db import models
from django.shortcuts import reverse

from funcionarios.models import Funcionario


class Documento(models.Model):
    nome = models.CharField(max_length=100)
    pertence = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    arquivo = models.FileField(upload_to='documentos')

    def get_absolute_url(self):
        return reverse('update_funcionario', args=[self.pertence.id])

    def __str__(self):
        return self.nome
