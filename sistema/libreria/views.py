from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return HttpResponse("<h1>Hello World</h1>")

def us(request):
    return render(request, 'pages/us.html')