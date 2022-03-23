import os, datetime
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'venyou.settings')
import django
django.setup()
from venyou_app.models import UserProfile, Venue, Event, Rating
from django.contrib.auth.models import User






def populate():


    #### VENUE DEFINITIONS FOR EACH OWNER ACCOUNT ####

    simons_venues = [
        {'name': 'Garage',
        'description': 'Popular venue for university students. It is Scotland\'s largest nightclub.',
        'address': '490 Sauchiehall St',
        'city':'Glasgow',
        'postcode':'G2 3LW',
        'latitude':55.86624,
        'longitude':-4.26830}
    ]

    leens_venues = [
        {'name':'Firewater',
        'description':'Music bar serving a range of hard liquor as well as American comfort food across 2 rooms.',
        'address':'341 Sauchiehall St',
        'city':'Glagsow',
        'postcode':'G2 3HW',
        'latitude':55.86572,
        'longitude':-4.26560},

        {'name':'Broadcast',
        'description':'Live music venue.',
        'address':'427 Sauchiehall St',
        'city':'Glagsow',
        'postcode':'G2 3LG',
        'latitude':55.86610,
        'longitude':-4.26907}
    ]

    iains_venues = [
        {'name':'Subclub',
        'description':'The Sub Club is a club and music venue. It opened 1 April 1987 and is the longest running underground dance club in the world.',
        'address': '22 Jamaica St',
        'city':'Glasgow',
        'postcode':'G1 4QD',
        'latitude':55.85798,
        'longitude':-4.25690},

        {'name':'Stereo',
        'description':'Performance space on ground floor of impressive building with imaginative vegan cafe/bar above.',
        'address':'22 Renfield Ln',
        'city':'Glasgow',
        'postcode':'G2 5AR',
        'latitude':55.86166,
        'longitude':-4.25756}
    ]

    admin_venues = [
        {'name':'Administrator\'s House',
        'description':'This is where the admin is done.',
        'address':'University Of Glasgow, Hillhead St',
        'city':'Glasgow',
        'postcode':'G12 8QE',
        'latitude':55.87345,
        'longitude':-4.28861}
    ]


    #### USER ACCOUNT DEFINITIONS ####

    users = [
        # Owner Accounts
        {'username': 'leen',
        'password': 'password',
        'is_owner': True,
        'venues': leens_venues},

        {'username': 'Simon',
        'password': 'password',
        'is_owner': True,
        'venues':simons_venues},

        {'username':'iain',
        'password':'3w2w9w',
        'is_owner':True,
        'venues':iains_venues},

        # Non owner accounts
        {'username':'bob_standar',
        'password':'5555',
        'is_owner':False},

        {'username':'jill',
        'password':'8888',
        'is_owner':False},

        {'username':'hacker',
        'password':'1234',
        'is_owner':False},
    ]

    #### CREATE SUPERUSER ACCOUNT ####


    
    #### RANDOM RATING DEFINITIONS ####

    ratings = [
        {'hygiene_score': '4',
        'vibe_score': '9.5',
        'safety_score': '10',
        'comment': 'It is very safe, well maintained, and has a hygiene score of 4/5',
        'date': datetime.datetime(2022, 3, 10, 14, 5, 32),
        'writer': 3, # Index in the account array
        'about': 2}

    ]


    #### RANDOM EVENT DEFINITIONS ####
    
    event= [
    {'name': 'Halloween',
    'description':'Fancy a night out on the scariest night of the year? We are offering free entry before 11 pm and 1.50 pound shots',
    'date':'31/10/2022',
    'organizer': 'Simon',
    'venue': 'Garage',
    'ticket_link': 'https://garageglasgow.co.uk/gig-listings/'
            }]
    
    created_users = []
    created_venues = []

    for user in users:
        new_user = add_user(user['username'], user['password'], user['is_owner'])
        created_users.append(new_user)
        if user['is_owner']:
            for venue in user['venues']:
                new_venue = add_venue(venue['name'], venue['description'], venue['address'], venue['city'],
                          venue['postcode'], venue['latitude'], venue['longitude'], new_user)
                created_venues.append(new_venue)
        
    for rating in ratings:
        writer = created_users[rating['writer']]
        about = created_venues[rating['about']]
        #new_rating = add_rating(rating['hygiene_score'], rating['vibe_score'], rating['safety_score'], 
        #                        rating['comment'], rating['date'], writer, about)
    
        


def add_user(username, password, is_owner):
    user= User.objects.get_or_create(username= username, password= password)[0]
    user.save()
    userprofile= UserProfile.objects.get_or_create(user= user, is_owner= is_owner)[0]
    userprofile.save()
    return userprofile

def add_venue(name, description, address, city, postcode, latitude, longitude, owner):
    venue= Venue.objects.get_or_create(name= name, description= description, 
                                        address= address, city=city, postcode=postcode,
                                        owner=owner, latitude=latitude, longitude=longitude)[0]
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
