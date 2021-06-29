
from django.urls import path
from .views import ClientesList, ClienteEdit


urlpatterns = [
    path('', ClientesList.as_view(), name='list_clientes'),
    path('editar/<int:pk>', ClienteEdit.as_view(), name='update_cliente'),
    # path('deletar/<int:pk>', FuncionarioDelete.as_view(), name='delete_funcionario'),
    # path('novo/', FuncionarioCreate.as_view(), name='creat_funcionario')
]

