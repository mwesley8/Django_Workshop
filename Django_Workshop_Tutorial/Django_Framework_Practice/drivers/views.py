#from django.shortcuts import render
import datetime
from django.template import loader
from django.http import HttpResponse
from .models import Driver

# Create your views here.
def drivers(request):
    allDrivers = Driver.objects.all()  #.values()
    template = loader.get_template('all_drivers.html')
    day = datetime.date.today().strftime('%m-%d-%Y')
    context = {
        'myDrivers': allDrivers,
        'Today': day
    }
    return HttpResponse(template.render(context, request))
    #1return HttpResponse("Maurice Unchained Django!")

def details(request, id):
    aDriver = Driver.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'myDriver': aDriver
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    day = datetime.date.today().strftime('%m-%d-%Y')
    allDrivers = Driver.objects.all() #.values()
    template = loader.get_template('testing1.html')
    context = {
        'trucks': ['Ken Worth', 'Freightliner', 'Peter Built', 'International'],
        'variable': 'Maurice',
        'Drivers': allDrivers,
        'Today': day
    }
    return HttpResponse(template.render(context, request))
