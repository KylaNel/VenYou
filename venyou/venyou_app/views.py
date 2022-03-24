from multiprocessing import context
from urllib.parse import urldefrag
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.core import serializers
import json

from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from venyou_app.models import UserProfile, Rating, Venue, Event

from venyou_app.forms import RatingsForm, VenueForm, UserProfileForm, UserForm

# Create your views here.

class StarRating:
    def __init__(self, ratings):
        self.has_been_rated = True
        if len(ratings) == 0:
            self.has_been_rated = False
        else:
            self.calculate_stars(ratings)

    def calculate_stars(self, ratings):

        # For each category of rating take an average
        hygiene_score = sum([rating.hygiene_score for rating in ratings])/len(ratings)
        vibe_score = sum([rating.vibe_score for rating in ratings])/len(ratings)
        safety_score = sum([rating.safety_score for rating in ratings])/len(ratings)

        # Calculate how many of each kind of star is needed
        self.st_hg_f, self.st_hg_h, self.st_hg_e = self.get_no_star_types(hygiene_score)
        self.st_vb_f, self.st_vb_h, self.st_vb_e = self.get_no_star_types(vibe_score)
        self.st_sf_f, self.st_sf_h, self.st_sf_e = self.get_no_star_types(safety_score)

    def get_no_star_types(self, score):
        """ 
        Returns a 3-tuple of how many full, half and empty stars are needed
        to represent a score. Returns ranges so that the django template can
        iterate over them.
        """
        rounded = round(score*2)/2

        no_full_stars = int(rounded//1)
        no_half_stars = int((rounded-no_full_stars+0.9)//1)
        no_empty_stars = int(5-no_full_stars-no_half_stars)

        print(no_full_stars, no_half_stars, no_empty_stars)

        return range(no_full_stars), range(no_half_stars), range(no_empty_stars)


def get_user_profile_or_none(request):
    try:
        user = User.objects.get(username=request.user.username)
        user_profile = UserProfile.objects.get(user=user)
    except (User.DoesNotExist, UserProfile.DoesNotExist) as e:
        return (None, None)
    return user, user_profile
        

@login_required
def rate(request, venue_name_slug):
    venue = get_object_or_404(Venue, name_slug=venue_name_slug)

    user, user_profile = get_user_profile_or_none(request)

    submit = False
    if  request.method == "POST":
        form = RatingsForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.about = venue
            rating.writer = user_profile
            rating.save()
            submit = True
            #return redirect(reverse('venyou_app:rate', kwargs={'venue_name_slug':venue_name_slug}))
    else:
        form = RatingsForm()
        #if 'submit' in request.GET:
        #    submit = True

    return render(request, 'venyou_app/rate.html', {'user_profile':user_profile, 'form': form, 'submit': submit, 'venue':venue})

def home(request):

    user, user_profile = get_user_profile_or_none(request)

    event_list = Event.objects.order_by('date')[:8]
    venue_list = Venue.objects.order_by('name')#[:3]

    context_dict = {}
    context_dict['events'] = event_list
    context_dict['venues'] = venue_list
    context_dict['user_profile'] = user_profile

    return render(request, 'venyou_app/home.html', context=context_dict)

def map(request):

    user, user_profile = get_user_profile_or_none(request)

    venues_serialized = serializers.serialize("json", Venue.objects.all())

    context_dict = {}
    context_dict['venues'] = json.loads(venues_serialized)
    context_dict['user_profile'] = user_profile
    return render(request, 'venyou_app/map.html', context=context_dict)

def search(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        venue = Venue.objects.all().filter(name=search)
        return render(request, 'venyou_app/search.html', {'venue': venue})
        

def user_login(request):
    user, user_profile = get_user_profile_or_none(request)

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('venyou_app:home'))
            else:
                return render(request, 'venyou_app/login.html', {'error':'Your account is disabled.', 'user_profile':user_profile})
        else:
            print(f"Invalid login details: {username}, {password}")
            return render(request, 'venyou_app/login.html', {'error':'Invalid login details supplied.', 'user_profile':user_profile})
    else:
        return render(request, 'venyou_app/login.html', {'user_profile':user_profile})

@login_required
def myaccount(request):
    user, user_profile = get_user_profile_or_none(request)

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

    user, user_profile = get_user_profile_or_none(request)

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
    user, user_profile = get_user_profile_or_none(request)

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
                    'created':already_created,
                    'user_profile':user_profile}
    return render(request, 'venyou_app/create_account.html',  context_dict)


def venue_page(request, venue_name_slug):

    user, user_profile = get_user_profile_or_none(request)

    context_dict = {}
    context_dict['user_profile'] = user_profile

    try:
        venue = Venue.objects.get(name_slug=venue_name_slug)
        context_dict['venue'] = venue

        ratings = Rating.objects.filter(about=venue)
        events = Event.objects.filter(venue=venue)

        star_rating = StarRating(ratings)
        context_dict['sr'] = star_rating
        context_dict['ratings'] = ratings
        context_dict['events'] = events

    except Venue.DoesNotExist:
        context_dict['venue'] = None

    return render(request, 'venyou_app/venue.html', context_dict)


def venue_browse(request):
    user, user_profile = get_user_profile_or_none(request)
    context_dict = {'venues':Venue.objects.all()}
    context_dict['user_profile'] = user_profile
    return render(request, 'venyou_app/venue_browse.html', context_dict)