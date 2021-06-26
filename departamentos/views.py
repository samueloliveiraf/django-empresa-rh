
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Departamento
from django.urls import reverse_lazy


class DepartamentoList(ListView):
    model = Departamento

    def get_queryset(self):
        empresa_Logada = self.request.user.funcionario.empresa
        queryset = Departamento.objects.filter(empresa=empresa_Logada)
        return queryset


class DepartamentoCreate(CreateView):
    model = Departamento
    fields = ['nome']
    
    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.funcionario.empresa
        departamento.save()
        return super(DepartamentoCreate, self).form_valid(form)


class DepartamentoUpdate(UpdateView):
    model = Departamento
    fields = ['nome']


class DepartamentoDelete(DeleteView):
    model = Departamento
    success_url = reverse_lazy('list_departamentos')
