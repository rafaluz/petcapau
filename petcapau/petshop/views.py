from django.shortcuts import render
from django.http import HttpResponse
from .models import Pet
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def helloWorld(request):
    mensagem = 'Olá, mundo!'
    return render(request, 'pet/hello_world.html', {'mensagem':mensagem})

# Listagem dos pets usando função
# def PetList(request):
#     pets = Pet.objects.all()
#     return render(request, 'pet/pet_list.html',{'pets': pets})

# def PetDetail(request, id):
#     pet = Pet.objects.get(id=id)
#     return render(request, 'pet/pet_detail.html',{'pet': pet})



class PetList(ListView):
    model = Pet
    template_name = 'pet/pet_list.html'


class PetDetail(DetailView):
    model = Pet
    template_name = 'pet/pet_detail.html'