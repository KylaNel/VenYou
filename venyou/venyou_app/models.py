from django.db import models
from django.contrib.auth.models import User
from django.forms import IntegerField

# Create your models here.

class UserProfile(models.Model):
    # To extend on the functionality of Django's user model
    # we create a one-to-one link with the user
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    picture = models.ImageField(upload_to='', blank=True)
    is_owner = models.BooleanField()

    def __str__(self):
        return self.user.username

class Venue(models.Model):
    NAME_MAX_LENGTH = 50
    DESC_MAX_LENGTH = 300
    ADDRESS_MAX_LENGTH = 100

    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    description = models.CharField(max_length=DESC_MAX_LENGTH)
    address = models.CharField(max_length=ADDRESS_MAX_LENGTH)

    def __str__(self):
        return self.name


class Rating(models.Model):
    COMMENT_MAX_LENGTH = 500
    
    hygiene_score = IntegerField(min_value=0, max_value=5)
    vibe_score = IntegerField(min_value=0, max_value=5)
    safety_score = IntegerField(min_value=0, max_value=5)

    comment = models.CharField(max_length=COMMENT_MAX_LENGTH, blank=True)
    date = models.DateField()


class Event(models.Model):
    pass