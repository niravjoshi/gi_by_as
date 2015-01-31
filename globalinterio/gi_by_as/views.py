# Django imports
from django.shortcuts import render
from django.http import HttpResponse

# App imports
from messages import messages as m

def home(request):
    context={}
    context['msg1'] = m['msg1']
    context['selected'] = "active"
    return render(request, 'home.html', context)

def aboutus(request):
    context={}
    context['about'] = "active"
    return render(request, 'about.html', context)

def services(request):
    context={}
    context['services'] = "active"
    return render(request, 'services.html', context)
 
def clients(request):
    context={}
    context['clients'] = "active"
    return render(request, 'clients.html', context)
 
def contact(request):
    context={}
    context['contact'] = "active"
    return render(request, 'contact.html', context)
