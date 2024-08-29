from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>Events - Home</h1>')

def about(request):
    return HttpResponse('<h1>Events - About</h1>')

def contact(request):
    return HttpResponse('<h1>Events - Contact</h1>')

def team(request):
    return HttpResponse('<h1>Events - Team</h1>')
