from django.shortcuts import render
from django.http import HttpResponse
from .models import Pet
# Create your views here.

def helloWorld(request):
    mensagem = 'Olá, mundo!'
    return render(request, 'pet/hello_world.html', {'mensagem':mensagem})


def PetList(request):
    pets = Pet.objects.all()
    return render(request, 'pet/pet_list.html',{'pets': pets})

def PetDetail(request, id):
    pet = Pet.objects.get(id=id)
    return render(request, 'pet/pet_detail.html',{'pet': pet})