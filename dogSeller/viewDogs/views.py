
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,context
# Create your views here.

# homepage
def homepage(request):
    # phones = Phones.objects.all()
    # accessories = Accessories.objects.all()
    # print(phones)
    # print(accessories)
    # params = {'products':phones}
    return render(request,'viewDogs/base.html')