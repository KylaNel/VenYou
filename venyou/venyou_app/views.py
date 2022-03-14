from django.shortcuts import render
from .forms import RatingsForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect


# Create your views here.


def index(request):
    return render(request, 'venyou_app/base.html')


def rate(request):
    submit = False
    if  request.method == "POST":
        form = RatingsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate?submit=True')
    else:
        form = RatingsForm()
        if 'submit' in request.GET:
            submit = True

    return render(request, 'venyou_app/rate.html', {'form': form, 'submit': submit})
    
def home(request):
    return render(request, 'venyou_app/home.html')

def map(request):
    return render(request, 'venyou_app/map.html')
