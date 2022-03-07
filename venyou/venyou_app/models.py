from django.db import models
from django.contrib.auth.models import User

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
    pass

class Event(models.Model):
    pass