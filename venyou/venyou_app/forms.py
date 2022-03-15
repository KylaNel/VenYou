from django import forms
from django.db import models
from django.forms import ModelForm
from django.core.validators import MaxValueValidator, MinValueValidator
from .models import Rating


class RatingsForm(forms.ModelForm):
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