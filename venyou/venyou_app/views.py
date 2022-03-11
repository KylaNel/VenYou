from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'venyou_app/home.html')

def map(request):
    return render(request, 'venyou_app/map.html')