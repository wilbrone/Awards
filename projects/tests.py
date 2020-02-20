from django.test import TestCase
from django.contrib.auth.models import User

from .models import *

# Create your tests here.


class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username='charles',email='example@gmail.com',password='sahara10322')
        self.user.save()

        self.profile_test = Profile(bio='this is a test profile', profile_pic='default.jpg', location='Nrb',user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile_test, Profile))

    def test_save_profile(self):
        after = Profile.objects.all()
        self.assertTrue(len(after) > 0)



class TestProject(TestCase):
    def setUp(self):
        # self.trialls = TestProfile()
        self.project_test = Project(title='Trial', image='default.png', image_url='https://test.com', description='default test')

    def test_instance(self):
        self.assertTrue(isinstance(self.project_test, Project))

    def test_save_image(self):
        self.project_test.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)

#     def test_delete_image(self):
#         self.image_test.delete_image()
#         after = Profile.objects.all()
#         self.assertTrue(len(after) < 1)