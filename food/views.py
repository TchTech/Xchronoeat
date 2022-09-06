from django.shortcuts import render
from .models import comfood
from django.db.models import Q

objects = comfood.objects.filter(name__icontains="пряник")

print(objects)

def index(request):
    return render(request, "index.html")

def search(request):
    query = request.GET.get("query")
    if query == "" or query == None:
        return render(request, "search.html", {"query": "", "foodLength":0, "searchedItems":{}})
    else:
        objects = comfood.objects.filter(name__icontains=query).__dict__
        print(objects)
        return render(request, "search.html", {"query": query, "foodLength":len(objects.keys()), "searchedItems":objects})
