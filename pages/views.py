
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'pages/index.html')

def iletisim(request):
    return render(request,'pages/contact.html')

def hakkimizda(request):
    return render(request,'pages/about.html')

# Create your views here.
