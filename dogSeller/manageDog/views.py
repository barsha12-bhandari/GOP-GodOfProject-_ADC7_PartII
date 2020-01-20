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


def updateDelete(request):
    ourdogs = Dogs.objects.all()
    params = {'dogs':ourdogs}
    return render(request,'manageDog/edel.html',params)


def update(request,ID):
    product = Dogs.objects.get(id=ID)
    context_varible = {'product':product}
    return render(request,'manageDog/update.html',context_varible)


def updateSave(request):
    dname = request.POST['Name']
    dbreed = request.POST['Breed']
    dprice = request.POST['Price']
    dweight = request.POST['Weight']
    ddescription = request.POST['Description']
    dstock = request.POST['Stock']

    ID = request.POST['dogID']
    # creating dog object
    dogObj = Dogs.objects.get(id=ID)

    if request.method == 'POST' and request.FILES['Image']:
        dimage=request.FILES['Image']
        fs = FileSystemStorage()
        filename = fs.save(dimage.name, dimage)
        file_url = fs.url(filename)
        dogObj.image = file_url

    
    dogObj.name = dname
    dogObj.breed = dbreed
    dogObj.price = dprice
    dogObj.weight = dweight
    dogObj.description = ddescription
    dogObj.stockNo = dstock
    dogObj.save()

    return HttpResponse("Dog details successfully updated")    