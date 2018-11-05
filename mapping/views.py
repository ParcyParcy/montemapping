import os
from django.http import HttpResponse
from django.shortcuts import render
from mymodule.plot_module import plot_mdl

base = os.path.dirname(os.path.abspath(__file__))
name = os.path.normpath(os.path.join(base, '../templates/data/sample.log'))


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def plot(request):
    plot_mdl(name)
    return render(request, 'map.html')
