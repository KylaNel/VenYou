import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'venyou.settings')
import django
django.setup()
from venyou_app.models import UserProfile, Venue, Event, Rating
from django.contrib.auth.models import User






def populate():

    Simons_venue= [
    {'name': 'Garage',
    'description': 'Popular venue for university students',
    'address': '490 Sauchiehall St, Glasgow G2 3LW'
            }]
    users= [
    {'username': 'leen',
    'password': 'password',
    'is_owner': True,
    'venues': []
            },
    {'username': 'Simon',
    'password': 'password',
    'is_owner': True,
    'venues':Simons_venue
           }]
    
    
    event= [
    {'name': 'Halloween',
    'description':'Fancy a night out on the scariest night of the year? We are offering free entry before 11 pm and 1.50 pound shots',
    'date':'31/10/2022',
    'organizer': 'Simon',
    'venue': 'Garage',
    'ticket_link': 'https://garageglasgow.co.uk/gig-listings/'
            }]
    
    rating= [{
    'hygiene_score': '4',
    'vibe_score': '9.5',
    'safety_score': '10',
     'comment': 'It is very safe, well maintained, and has a hygiene score of 4/5',
     'date': '10/03/22',
     'writer': 'Edward Smith',
     'about': 'about'
             }]
    
    for user in users:
        new_user= add_user(user['username'], user['password'], user['is_owner'])
        for venue in user['venues']:
            add_venue(venue['name'], venue['description'], venue['address'], new_user)
        
    for rating in ratings:
        new_rating= add_rating(rating['hygiene score'], rating['vibe_score'], rating['safety_score'], rating['comment'], rating['comment'], rating['date'], rating['writer'], rating['about'])
    
        


def add_user(username, password, is_owner):
    user= User.objects.get_or_create(username= username, password= password)[0]
    user.save()
    userprofile= UserProfile.objects.get_or_create(user= user, is_owner= is_owner)[0]
    userprofile.save()
    return userprofile

def add_venue(name, description, address, owner):
    venue= Venue.objects.get_or_create(name= name, description= description, address= address, owner=owner)[0]
    venue.save()
    return Venue

def add_event(name, description, date, organizer, venue, ticket_link):
    event = Event.objects.get_or_create(name= name, description= description, date= date, organizer= organizer, venue= venue, ticket_link= ticket_link)[0]
    event.save()
    return event

def add_rating(hygiene_score, vibe_score, safety_score, comment, date, writer, about):
    rating= Rating.objects.get_or_create(hygiene_score= hygiene_score, vibe_score= vibe_score, safety_score= safety_score, comment= comment, date= date, writer= writer, about= about)[0]
    rating.save()
    return rating


if __name__=='__main__':
    print('Populating Venyou_app database...')
    populate()
