# Django imports
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context={}
    return render(request, 'base.html', context)
    #return HttpResponse("Hello Nirav.")
