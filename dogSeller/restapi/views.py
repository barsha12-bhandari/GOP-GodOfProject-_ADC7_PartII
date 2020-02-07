from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from viewDogs.models import Dogs
import json
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User, Group

# Create your views here.

# Get a specific model data by ID => GET
# http://127.0.0.1:8000/api/getDogDetails/1
@csrf_exempt
def getDogDetails(request,ID):
    if request.method == "GET":
        try:
            dog = Dogs.objects.get(id = ID)
        except Dogs.DoesNotExist:
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

# Get all model data => GET
# http://127.0.0.1:8000/api/getAllDogs/     
@csrf_exempt
def getAllDogs(request):
    if request.method == "GET":
        dogs = Dogs.objects.all()
        list_of_dogs = list(dogs.values("name","price","id","breed","weight"))
        dogDictionary = {
            "dogs":list_of_dogs
        }
        return JsonResponse(dogDictionary)

    else:
        return JsonResponse({
            "message":"Only get request available"
        })


# Post model data => POST
# http://127.0.0.1:8000/api/createUser/
# {"Username":"testuser","Password":"test@password","Email":"testuser@dogseller.com","Fname":"Sarnesh","Lname":"Raj Pandit"}
@csrf_exempt
def createUser(request):
    if request.method == 'POST':
        dictionary_object = json.loads(request.body)
        user = User.objects.create_user(username=dictionary_object['Username'],password=dictionary_object['Password'],email=dictionary_object['Email'],first_name=dictionary_object['Fname'],last_name=dictionary_object['Lname'])
        user.save()
        
        return JsonResponse({
            "message":"Successfully created user"
        })

    else:
        return JsonResponse({
            "message":"Only POST request available"
        })

#Update a specific model data by ID => PUT
#http://127.0.0.1:8000/api/updateDogPrice/
#{"id":"3","price":"105000"}
@csrf_exempt
def updateDogPrice(request):
    if request.method == 'PUT':
        dictionary_object = json.loads(request.body)
        dog = Dogs.objects.get(id=dictionary_object['id'])
        dog.price = id=dictionary_object['price']
        dog.save()
        return JsonResponse({
            "message":"Successfully updated price"
        })
    
    else:
        return JsonResponse({
            "message":"Only PUT request available"
        })

# Delete a specific model data by ID => DELETE
# http://127.0.0.1:8000/api/deleteDog/4
@csrf_exempt
def deleteDog(request,ID):
    if request.method == 'DELETE':
        Dogs.objects.get(id=ID).delete()
        return JsonResponse({
            "message":"Successfully deleted dog"
        })
    
    else:
        return JsonResponse({
            "message":"Only Delete request available"
        })