from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from receitas.forms import PostForm
from rest_framework import viewsets
from .models import Receita
from django.http import HttpResponse


def index(request):

    receitas= Receita.objects.all()

    dados = {
        'receitas': receitas
    }
    return render(request,'index.html', dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    exibe_receita = {
        'receita':receita
    }

    return render(request, 'receita.html',exibe_receita)

class ReceitaCreate(CreateView):
    model = Receita
    fields = ['nome_receita','ingredientes','preparo','tempo_preparo',
        'rendimento','categoria','dt_prepato','file_name']
    template_name = 'account/form.html'
    success_url = reverse_lazy('index')



#------------------UPDATE---------------------------#

class ReceitaUpdate(UpdateView):
    model = Receita
    fields = ['nome_receita','ingredientes','preparo','tempo_preparo',
        'rendimento','categoria','dt_prepato','file_name']
    template_name = 'account/form.html'
    success_url = reverse_lazy('index')


#------------------DELETE------------------------------#
       
class ReceitaDelete(DeleteView):
    model = Receita
    template_name = 'account/excluir.html'
    success_url = reverse_lazy('index')