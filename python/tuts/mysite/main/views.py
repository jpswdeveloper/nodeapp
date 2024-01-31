from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDO, Item

# Create your views here.


def index(response):
    return HttpResponse("<h1>Hello World from index route</h1>")


def v1(response, id):
    query = ToDO.objects.get(id=id)
    item = query.item_set.get(id=1)
    return HttpResponse(
        f"<h1>data comes from databases 1: Todo list name is {query.name} {item.text}</h1>"
    )
