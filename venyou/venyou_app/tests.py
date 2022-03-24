from datetime import datetime, tzinfo
import pytz
from django.test import TestCase
from venyou_app.models import UserProfile, Rating, Venue, Event
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class UserProfileTests(TestCase):

    def setUp(self):
        self.testUser = User.objects.get_or_create(username='testuser', password='password1234')[0]
        self.testProfile = UserProfile.objects.create(user=self.testUser, is_owner=True)

    def test_username_correct(self):
        """
            Tests that the user has been created correctly and the username is correct
        """

        self.assertEquals(self.testUser.username, 'testuser')

    def test_one_to_one_user_link(self):
        """
            Assert that the test user and the link to the user in the test profile are the same
        """

        self.assertEquals(self.testUser.username, self.testProfile.user.username)

    def test_is_onwer_field(self):
        """
            Tests the is_owner field has been set correctly
        """

        self.assertEquals(self.testProfile.is_owner, True)

class VenueTests(TestCase):
    
    def setUp(self):
        self.testUser = User.objects.get_or_create(username='testuser', password='password1234')[0]
        self.testProfile = UserProfile.objects.create(user=self.testUser, is_owner=True)
        self.testVenue = Venue.objects.create(name='test venue', description='A venue for the test cases',
                        address='1 Hacker Way', city='Glasgow', postcode='TE5 TS00',
                        latitude=-3.234343, longitude=10.000023, owner=self.testProfile)

    def test_creation_name_correct(self):
        """
            Assert hte object has been created correctly by checking the name
        """

        self.assertEquals(self.testVenue.name, 'test venue')

    def test_slugify_of_name(self):
        """
            Assert the slugifying of the name has worked correctly
        """

        self.assertEquals(slugify(self.testVenue.name), self.testVenue.name_slug)

    def test_owner_forigen_key(self):
        """
            Check the link to the owner profile works and see if the owner is a venue owner
        """

        self.assertTrue(self.testVenue.owner.is_owner)

    def test_type_of_longitude_field(self):
        """
            Test that the longitude field stores floating point numbers
        """

        self.assertEquals(type(self.testVenue.longitude), type(0.0))

class EventTests(TestCase):
    
    def setUp(self):
        self.testUser = User.objects.get_or_create(username='testuser', password='password1234')[0]
        self.testProfile = UserProfile.objects.create(user=self.testUser, is_owner=True)
        self.testVenue = Venue.objects.create(name='test venue', description='A venue for the test cases',
                        address='1 Hacker Way', city='Glasgow', postcode='TE5 TS00',
                        latitude=-3.234343, longitude=10.000023, owner=self.testProfile)
        self.testEvent = Event.objects.create(name='Test Event', description='A testing party: test all night long',
                        date=datetime.now(tz=pytz.UTC), venue=self.testVenue, organiser=self.testProfile,
                        ticket_link='www.test.com')

    def test_creation_by_description(self):
        """
            Assert the object is created with the correct description
        """

        self.assertEquals(self.testEvent.description, 'A testing party: test all night long')

    def test_link_to_venue(self):
        """
            Assert that the test event is linked correctly with the venue
        """

        self.assertEquals(self.testEvent.venue.id, self.testVenue.id)

    def test_link_to_organiser(self):
        """
            Assert that the test event is linked correctly with the user profile of the organiser
        """

        self.assertEquals(self.testEvent.organiser.id, self.testProfile.id)

    def test_datetime_is_set_correctly(self):
        """
            Check that the date which was created is now at least the same or in the past.
        """

        self.assertLessEqual(self.testEvent.date, datetime.now(tz=pytz.UTC))

class RatingMethodTests(TestCase):

    def setUp(self):
        self.testUser = User.objects.get_or_create(username='testuser', password='password1234')[0]
        self.testProfile = UserProfile.objects.create(user=self.testUser, is_owner=True)
        self.testVenue = Venue.objects.create(name='test venue', description='A venue for the test cases',
                        address='1 Hacker Way', city='Glasgow', postcode='TE5 TS00',
                        latitude=-3.234343, longitude=10.000023, owner=self.testProfile)
        self.testRating = Rating.objects.create(hygiene_score=4, vibe_score=2, safety_score=4,
                        comment='I enjoyed this test', date=datetime.now(tz=pytz.UTC), writer=self.testProfile,
                        about=self.testVenue)



    def test_hygiene_score_creation(self):
        """
            Ensures that the rating object is created correctly
        """

        rating = Rating.objects.create(hygiene_score = 2, vibe_score = 4, safety_score = 3,
                         comment="Test case", about=self.testVenue, writer=self.testProfile)        
        rating.save()
        self.assertEquals((rating.hygiene_score), 2)

    def test_successful_comment(self):
        """
            Asserts that the rating was created with the correct comment
        """

        self.assertEquals(self.testRating.comment, 'I enjoyed this test')

    def test_rating_date_is_in_past_or_equal(self):
        """
            Ensures the datetime was set correctly and is now in the past or equal
        """

        self.assertLessEqual(self.testRating.date, datetime.now(tz=pytz.UTC))

    def test_writer_relationship(self):
        """
            Assert the foriegn key stored in the rating's model links to the correct user profile
        """

        self.assertEquals(self.testRating.writer.user.username, 'testuser')

    def test_about_relationship(self):
        """
            Assert the foriegn key stored to the venue the rating is about is correc
        """

        self.assertEquals(self.testRating.about.name, 'test venue')