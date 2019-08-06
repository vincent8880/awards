from django.test import TestCase
from .models import countries,Project
from django.contrib.auth.models import User

# Create your tests here.
class countriesTestClass(TestCase):
    def setUp(self):
        self.Kenya = countries(countries='Kenya')

    def test_instance(self):
        self.assertTrue(isinstance(self.Kenya,countries))

    def tearDown(self):
        countries.objects.all().delete()

    def test_save_method(self):
        self.Kenya.save_country()
        country = countries.objects.all()
        self.assertTrue(len(country)>0)

    def test_delete_method(self):
        self.Kenya.delete_country('Kenya')
        country = countries.objects.all()
        self.assertTrue(len(country)==0)
class ProjectTestClass(TestCase):
    def setUp(self):
        self.triangle = countries(Project='triangle')

    def test_instance(self):
        self.assertTrue(isinstance(self.triangle,Project))

    def tearDown(self):
        Project.objects.all().delete()

    def test_save_method(self):
        self.Project.save_project()
        project= Project.objects.all()
        self.assertTrue(len(project)>0)

    def test_delete_method(self):
        self.triangle.delete_project('Kenya')
        project = Project.objects.all()
        self.assertTrue(len(project)==0)
