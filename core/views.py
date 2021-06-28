
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from funcionarios.models import Funcionario
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


@login_required
def home(request):
    data = {}
    data['usuario'] = request.user
    return render(request, 'index.html', data)


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'register.html'
