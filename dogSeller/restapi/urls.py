from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('getDogDetails/<int:ID>',getDogDetails),
    path('getAllDogs/',getAllDogs),
    path('createUser/',createUser),
    path('updateDogPrice/',updateDogPrice),
    path('deleteDog/<int:ID>',deleteDog),
    # pagination URL
    path('pagination/<int:SIZE>/<int:PAGENO>',getPage),
]