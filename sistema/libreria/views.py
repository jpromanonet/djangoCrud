from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def us(request):
    return render(request, 'pages/us.html')

def books(request):
    return render(request, 'books/index.html')

def addBooks(request):
    return render(request, 'books/add.html')