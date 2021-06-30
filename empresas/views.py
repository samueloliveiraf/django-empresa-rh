
from django.http.response import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView
from .models import Empresa
from django.urls import reverse_lazy


class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['nome']

    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()
        url = reverse_lazy('home')
        return HttpResponseRedirect(url)
    

class EmpresaEdit(UpdateView):
    model = Empresa
    fields = ['nome']

