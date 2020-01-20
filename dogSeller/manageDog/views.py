from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from viewDogs.models import Dogs
from django.http import HttpResponse
from django.template import Template,context
# Create your views here.
def adminDashboard(request):
    return render(request,'manageDog/dash.html')

def addDogForm(request):
    return render(request,'manageDog/add.html')

def saveDogs(request):
    dname = request.POST['Name']
    dbreed = request.POST['Breed']
    dprice = request.POST['Price']
    dweight = request.POST['Weight']
    ddescription = request.POST['Description']
    dstock = request.POST['Stock']

    if request.method == 'POST' and request.FILES['Image']:
        dimage=request.FILES['Image']
        fs = FileSystemStorage()
        filename = fs.save(dimage.name, dimage)
        file_url = fs.url(filename)

    dogObj = Dogs(name=dname,breed=dbreed,price=dprice,weight=dweight,description=ddescription,image=file_url,stockNo=dstock)
    dogObj.save()

    return HttpResponse("Dog details success fully saved")

def updateDelete(response):
    return render(request,'manageDog/edel.html')

