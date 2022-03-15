from django.shortcuts import render, redirect
from django.urls import reverse


from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from venyou_app.forms import RatingsForm
from venyou_app.models import UserProfile, Rating, Venue

# Create your views here.

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

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('venyou_app:home'))
            else:
                ## User is not active
                ## CHANGE THIS
                return HttpResponse('Your account is disabled.')
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse('Invalid login details supplied.')
    else:
        return render(request, 'venyou_app/login.html')

@login_required
def myaccount(request):

    user = User.objects.get(username=request.user.username)
    user_profile = UserProfile.objects.get(user=user)

    ratings = Rating.objects.filter(writer=user_profile)

    context_dict = {'user_profile':user_profile, 'ratings':ratings, }
    return render(request, 'venyou_app/myaccount.html', context=context_dict)
