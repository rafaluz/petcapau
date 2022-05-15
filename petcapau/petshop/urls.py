from django.urls import path
from . import views

app_name = "petshop"

urlpatterns = [
    path('helloworld/', views.helloWorld),
    path('pet/list', views.PetList, name='pet_list'),
    path('pet/detail/<int:id>', views.PetDetail, name='pet_detail'),
]
