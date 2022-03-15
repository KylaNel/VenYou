from multiprocessing import context
from django.shortcuts import render, redirect
from django.urls import reverse

from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from venyou_app.models import UserProfile, Rating, Venue

from venyou_app.forms import RatingsForm, VenueForm, UserProfileForm, UserForm

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
                return render(request, 'venyou_app/login.html', {'error':'Your account is disabled.'})
        else:
            print(f"Invalid login details: {username}, {password}")
            return render(request, 'venyou_app/login.html', {'error':'Invalid login details supplied.'})
    else:
        return render(request, 'venyou_app/login.html')

@login_required
def myaccount(request):

    user = User.objects.get(username=request.user.username)
    user_profile = UserProfile.objects.get(user=user)

    ratings = Rating.objects.filter(writer=user_profile)
    venues = Venue.objects.filter(owner=user_profile)

    context_dict = {'user_profile':user_profile, 'ratings':ratings, 'venues':venues}
    return render(request, 'venyou_app/myaccount.html', context=context_dict)

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('venyou_app:home'))

@login_required
def add_venue(request):
    form = VenueForm()

    user = User.objects.get(username=request.user.username)
    user_profile = UserProfile.objects.get(user=user)
    if user_profile and user_profile.is_owner:

        if request.method == 'POST':
            form = VenueForm(request.POST)
            if form.is_valid():
                venue = form.save(commit=False)
                venue.owner = user_profile
                venue.save()
                return redirect(reverse('venyou_app:myaccount'))
        
        context_dict = {'user_profile':user_profile, 'form':form}
        return render(request, 'venyou_app/add_venue.html', context_dict)
    else:
        return redirect(reverse('venyou_app:myaccount'))

def create_account(request):


    already_created = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        user_profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and user_profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user_profile = user_profile_form.save(commit=False)
            user_profile.user = user

            if 'picture' in request.FILES:
                user_profile.picture = request.FILES['picture']

            user_profile.save()

            login(request, user)
            already_created = True

    else:
        user_form = UserForm()
        user_profile_form = UserProfileForm()
    
    context_dict = {'user_form':user_form,
                    'user_profile_form':user_profile_form,
                    'created':already_created}
    return render(request, 'venyou_app/create_account.html',  context_dict)


def venue_page(request, venue_name_slug):

    context_dict = {}

    try:
        venue = Venue.objects.get(name_slug=venue_name_slug)
        context_dict['venue'] = venue

    except Venue.DoesNotExist:
        context_dict['venue'] = None

    return render(request, 'venyou_app/venue.html', context_dict)