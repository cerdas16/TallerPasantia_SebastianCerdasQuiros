from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):

    return HttpResponse("Hola, Mundo, Tu estás mirando el index de polls")