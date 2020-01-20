
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,context
from viewDogs.models import Dogs
# Create your views here.

# homepage
def homepage(request):
    ourdogs = Dogs.objects.all()
    params = {'dogs':ourdogs}
    return render(request,'viewDogs/home.html',params)


def viewProductDetails(request,ID):
    product = Dogs.objects.get(id=ID)
    context_varible = {'product':product}
    return render(request,'viewDogs/view.html',context_varible)