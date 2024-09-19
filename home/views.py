from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDo

# Create your views here.
def index(response, id):
    ls = ToDo.objects.get(id=id)
    return render(response, "home/base.html", {"name": ls.name})


def home(response):
    return render(response, "home/home.html", {"name": "test"})

    