from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>Category - Home</h1>')

def about(request):
    return HttpResponse('<h1>Category - About</h1>')

def contact(request):
    return HttpResponse('<h1>Category - Contact</h1>')

def team(request):
    return HttpResponse('<h1>Category - Team</h1>')