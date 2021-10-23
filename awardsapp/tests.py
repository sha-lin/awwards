from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Project, Rating
import datetime as dt

class ProfileTestClass(TestCase):
    def setUp(self):
        self.profile = Profile(user='montez', bio='coolbeans', profile_photo='cloudlink.cloud')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))
   
class ProjectTestClass(TestCase):
    def setUp(self):
        self.project = Project(title='tessaract', project_image='cloudlink.cloud', description='3D interpretation of a 4D object', link='tess.com', pub_date='2020', prof_ref='MontezProfile')

    def test_instance(self):
        self.assertTrue(isinstance(self.project, Project))

class RatingTestClass(TestCase):
    def setUp(self):
        self.rating = Rating(user='montez', project='tessaract', review='mind-boggling', rate_design=10, rate_usability=9, rate_content=8)

    def test_instance(self):
        self.assertTrue(isinstance(self.rating, Rating))
