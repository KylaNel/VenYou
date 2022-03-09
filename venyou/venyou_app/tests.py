from datetime import datetime
from django.test import TestCase
from venyou.venyou_app.models import UserProfile

from venyou_app.models import Rating

# Create your tests here.

class RatingMethodTests(TestCase):

    def test_hygiene_score_is_in_range(self):

        ## BROKEN TEST NEEDS MORE WORK
        """
            Ensures that the score given for hygiene is between 1 and 5 inclusive
        """

        rating = Rating(hygiene_score = 0, vibe_score = 4, safety_score = 3,
                         comment="Test case worked fine", date=datetime.now())

        
        
        rating.save()
        
        self.assertEquals((rating.hygiene_score), 0)