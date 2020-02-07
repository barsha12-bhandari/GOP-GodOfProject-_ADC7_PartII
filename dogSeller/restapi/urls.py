from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('api/getDogDetails/<int:ID>',getDogDetails),
    # path('getAllDogs/',getAllProducts),
    # path('createUser/',createUser),
    # path('updateDogPrice/',updateProductPrice),
    # path('deleteDog/<int:ID>',deleteProduct),
]