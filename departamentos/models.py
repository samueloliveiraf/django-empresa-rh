from django.urls import reverse
from django.db import models
from django.db.models.deletion import PROTECT
from empresas.models import Empresa


class Departamento(models.Model):
    nome = models.CharField(max_length=100)
    empresa = models.ForeignKey(Empresa, on_delete=PROTECT)

    def get_absolute_url(self):
        return reverse('list_departamentos')

    def __str__(self):
        return self.nome
