from django.shortcuts import render
from django.http import *
from django.template import loader

from .models import *

######

def index(request):
    template = loader.get_template('simulator/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def run(request):
    template = loader.get_template('simulator/run.html')
    context = {}
    return HttpResponse(template.render(context, request))