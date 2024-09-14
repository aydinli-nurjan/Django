from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import *

# Create your views here.
# def html(request):
#     posts = News.objects.all()
#     return render(request, 'news/index.html', {'posts': posts, 'title': 'Main page'})

# def index(request, catid):
#     return HttpResponse(f'<h1>News - Home</h1><p>{catid}</p>')

# def about(request, cat):
#     return HttpResponse(f'<h1>News - About</h1><p>{cat}</p>')

def home(request):
    return render(request, 'news/index.html')

def contact(request):
    return render(request, 'news/contact.html')


def single_page(request):
    return render(request, 'news/single-page.html')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>News - pageNotFound</h1>')