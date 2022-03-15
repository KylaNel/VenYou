from django.contrib import admin
from venyou_app.models import UserProfile, Event, Venue, Rating

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Event)
admin.site.register(Venue)
admin.site.register(Rating)