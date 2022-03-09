import os
import django
from venyou_app.models import UserProfile, Venue, Event, Rating

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'venyou.settings')
django.setup()



def populate():
    pass



def add_user():
    pass

def add_venue():
    pass

def add_event():
    pass

def add_rating():
    pass


if __name__=='__main__':
    print('Populating Venyou_app database...')
    populate()