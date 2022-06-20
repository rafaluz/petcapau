from django.shortcuts import render
from django.http import HttpResponse
from .models import Pet
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.db.models import Q

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        pets = Pet.objects.all()
        
        if self.request.GET.get('search_box'):
            search_box = self.request.GET['search_box']
            pets = Pet.objects.filter(Q(name__icontains = search_box) | Q(breed__icontains = search_box))

        context.update({
            'object_list': pets,
            })

        return context


class PetDetail(DetailView):
    model = Pet
    template_name = 'pet/pet_detail.html'

class PetCreate(CreateView):
    model = Pet
    template_name = 'pet/pet_create.html'
    fields = ['name','species','breed','sex','birth_date','hair','tatoo']

    def get_success_url(self):
        return reverse('petshop:pet_list')

class PetUpdate(UpdateView):
    model = Pet
    template_name = 'pet/pet_create.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('petshop:pet_list')

class PetDelete(DeleteView):
    model = Pet
    template_name = 'pet/pet_confirm_delete.html'
    success_url = reverse_lazy('petshop:pet_list')
    