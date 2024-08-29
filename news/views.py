from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>News - Home</h1>')

def about(request):
    return HttpResponse('<h1>News - About</h1>')

def contact(request):
    return HttpResponse('<h1>News - Contact</h1>')

def team(request):
    return HttpResponse('<h1>News - Team</h1>')