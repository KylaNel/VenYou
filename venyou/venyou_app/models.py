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
    pass

class Rating(models.Model):
    pass

class Event(models.Model):
    pass