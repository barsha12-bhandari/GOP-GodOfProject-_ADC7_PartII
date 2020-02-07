from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from viewDogs.models import Dogs
import json
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User, Group

# Create your views here.
@csrf_exempt
def getDogDetails(request,ID):
    if request == "GET":
        try:
            dog = Doobjects.get(id = ID)
        except Product.DoesNotExist:
            return JsonResponse({
                "dog":"none"
            })
        img = str(dog.image.url)
        return JsonResponse({
                "id":dog.id,
                "name":dog.name,
                "price":dog.price,
                "image":img,
                "breed":dog.breed,
                "weight":dog.weight,
                "description":dog.description
            })

    else:
        return JsonResponse({
            "message":"Only get request available"
        })
        
