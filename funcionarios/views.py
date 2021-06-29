
from django.contrib.auth.models import User
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Funcionario
from django.urls import reverse_lazy


class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_Logada = self.request.user.funcionario.empresa
        queryset = Funcionario.objects.filter(empresa=empresa_Logada)
        return queryset

class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos', 'salario']


class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')


class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['nome', 'salario', 'departamentos']
    success_url = reverse_lazy('list_funcionarios')


    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username = funcionario.nome
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        return super(FuncionarioCreate, self).form_valid(form)

