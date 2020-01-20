from django.shortcuts import render
from django.template import Template,context
from viewDogs.models import Dogs
# Create your views here.

def view_search(request):
    query=request.GET['query']
    if len(query)>78:
        dogs=[]
    else:    
        dogs= Dogs.objects.filter(name__icontains=query)
    context_variable={'dogs': dogs, 'query': query}
    return render(request,'search/search.html',context_variable)
