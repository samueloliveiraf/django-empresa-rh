
from django.urls import path
from .views import ClientesList, ClienteEdit, ClienteDelete, ClienteCreate


urlpatterns = [
    path('', ClientesList.as_view(), name='list_clientes'),
    path('editar/<int:pk>', ClienteEdit.as_view(), name='update_cliente'),
    path('deletar/<int:pk>', ClienteDelete.as_view(), name='delete_cliente'),
    path('novo/', ClienteCreate.as_view(), name='creat_cliente')
]

