from django import forms
from django.db import models
from django.forms import ModelForm
from django.core.validators import MaxValueValidator, MinValueValidator

from venyou_app.models import Rating, Venue, UserProfile
from django.contrib.auth.models import User


class RatingsForm(ModelForm):
    class Meta:
        model = Rating
        fields = ('hygiene_score', 'vibe_score', 'safety_score',
                  'comment')
        labels = {
            'hygiene_score': '',
            'vibe_score': '',
            'safety_score': '',
            'comment': '',
        }
        widgets = {
            'hygiene_score': forms.TextInput(attrs={'class': 'form-control', 'type' : 'number'  ,'placeholder': 'Rate hygiene score out of 5'}),
            'vibe_score': forms.TextInput(attrs={'class': 'form-control', 'type': 'number','placeholder': 'Rate the vibe score out of 5'}),
            'safety_score': forms.TextInput(attrs={'class': 'form-control','type' : 'number', 'placeholder': 'Rate the safety score out of 5'}),
            'comment': forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': 'Any other comments?'}),
        }


class VenueForm(ModelForm):
    name = forms.CharField(max_length=Venue.NAME_MAX_LENGTH,
                          help_text="Venue Name:")
    description = forms.CharField(max_length=Venue.DESC_MAX_LENGTH,
                            help_text="Description:")
    address = forms.CharField(max_length=Venue.ADDRESS_MAX_LENGTH,
                            help_text="Address:")

    class Meta:
        model = Venue
        exclude = ('owner',)


class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture', 'is_owner')
