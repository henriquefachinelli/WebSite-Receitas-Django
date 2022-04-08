from django.urls import path

from receitas.models import Receita
from . import views
from .views import ReceitaCreate, ReceitaDelete, ReceitaUpdate


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:receita_id>', views.receita, name='receita'),
    path('criar/', ReceitaCreate.as_view(), name='addreceita'), 
    
    path('editar/<int:pk>', ReceitaUpdate.as_view(), name='editar-receita'),

    path('excluir/<int:pk>', ReceitaDelete.as_view(), name='excluir-receita'),
]