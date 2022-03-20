from datetime import datetime
from django.test import TestCase
from venyou_app.models import UserProfile, Rating, Venue, Event
from django.contrib.auth.models import User

# Create your tests here.

class RatingMethodTests(TestCase):

    def setUp(self):
        self.testUser = User.objects.get_or_create(username='testuser', password='password1234')[0]
        self.testProfile = UserProfile.objects.create(user=self.testUser, is_owner=True)
        self.testVenue = Venue.objects.create(name='test venue', description='A venue for the test cases',
                        address='1 Hacker Way', city='Glasgow', postcode='TE5 TS00',
                        latitude=-3.234343, longitude=10.000023, owner=self.testProfile)
        self.testEvent = Event.objects.create(name='Test Event', description='A testing party: test all night long',
                        date=datetime.now(), venue=self.testVenue, organiser=self.testProfile,
                        ticket_link='www.test.com')
        self.testRating = Rating.objects.create(hygiene_score=4, vibe_score=2, safety_score=4,
                        comment='I enjoyed this test', date=datetime.now(), writer=self.testProfile,
                        about=self.testVenue)



    def test_hygiene_score_is_in_range(self):
        """
            Ensures that the score given for hygiene is between 1 and 5 inclusive
        """

        rating = Rating.objects.create(hygiene_score = 8, vibe_score = 4, safety_score = 3,
                         comment="Test case", about=self.testVenue, writer=self.testProfile)
    
        
        rating.save()

        self.assertEquals((rating.hygiene_score), 8)