from django.urls import path
from . import views

app_name = "petshop"

urlpatterns = [
    path('helloworld/', views.helloWorld),
    # path('pet/list', views.PetList, name='pet_list'),
    path('pet/list', views.PetList.as_view(), name='pet_list'),
    # path('pet/detail/<int:id>', views.PetDetail, name='pet_detail'),
    path('pet/detail/<int:pk>', views.PetDetail.as_view(), name='pet_detail'),
    path('pet/create', views.PetCreate.as_view(), name='pet_create'),
    path('pet/update/<int:pk>', views.PetUpdate.as_view(), name='pet_update'),
]
