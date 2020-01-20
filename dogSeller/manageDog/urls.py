from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', adminDashboard),
    path('add/',addDogForm),
    path('add/save', saveDogs),
    path('edel/',updateDelete),
    path('update/<int:ID>', update),
    path('update/save/', updateSave)
    # path('viewAccessories/',seeAccessories),
]