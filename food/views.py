from turtle import title
from django.shortcuts import render
from .models import CommonFood
from django.db.models import Q
import json
import os
from pathlib import Path

APP_TITLE = "ИнфоЕда"

BASE_DIR = Path(__file__).resolve().parent

image_to_label = {}

with open(os.path.join(os.path.dirname(BASE_DIR), "food", "label_to_image.json"), "r", encoding="utf-8") as f:
    image_to_label = json.load(f)

print(image_to_label)

def index(request):
    return render(request, "index.html", {"title": APP_TITLE})

def search(request):
    query = request.GET.get("query")
    if query == "" or query == None:
        return render(request, "search.html", {"query": "", "foodLength":0, "searchedItems":{}, "title":APP_TITLE})
    else:
        objects = CommonFood.objects.filter(name__icontains=query).values()
        for i in range(objects.__len__()):
            objects[i]["image"] = "food/img/comfood/"+image_to_label[objects[i]["category"]]
            
        return render(request, "search.html", {"query": query, "foodLength":objects.__len__(), "searchedItems":objects, "title":APP_TITLE})
