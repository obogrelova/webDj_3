from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, "main/index.html")

def newpage2(request):
    return render(request, "main/newpage2.html")

def newpage3(request):
    return render(request, "main/newpage3.html")

def newpage4(request):
    return render(request, "main/newpage4.html")