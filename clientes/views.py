
from .models import Cliente
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.contrib.auth.models import User


class ClientesList(ListView):
    model = Cliente

    def get_queryset(self):
        empresa_Logada = self.request.user.funcionario.empresa
        queryset = Cliente.objects.filter(empresa=empresa_Logada)
        return queryset


class ClienteEdit(UpdateView):
    model = Cliente
    fields = ['nome', 'cpf']

