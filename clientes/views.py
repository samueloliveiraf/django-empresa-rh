
from .models import Cliente
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy


class ClientesList(ListView):
    model = Cliente

    def get_queryset(self):
        empresa_Logada = self.request.user.funcionario.empresa
        queryset = Cliente.objects.filter(empresa=empresa_Logada)
        return queryset


class ClienteEdit(UpdateView):
    model = Cliente
    fields = ['nome', 'cpf', 'cep', 'numero', 'rua']


class ClienteDelete(DeleteView):
    model = Cliente
    success_url = reverse_lazy('list_funcionarios')


class ClienteCreate(CreateView):
    model = Cliente
    fields = ['nome', 'cpf', 'cep', 'numero', 'rua']
    success_url = reverse_lazy('list_clientes')

    def form_valid(self, form):
        cliente = form.save(commit=False)
        cliente.empresa = self.request.user.funcionario.empresa
        cliente.save()
        return super(ClienteCreate, self).form_valid(form)


