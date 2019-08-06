from django.db import models
from pyuploadcare.dj.models import ImageField
from django.contrib.auth.models import User
from django.db.models import Q

# Create your models here.
class countries(models.Model):
    countries = models.CharField(blank=True,max_length=100)

    def __str__(self):
        return self.countries

    class Meta:
        ordering = ['countries']


    def save_country(self):
        self.save()

    @classmethod
    def delete_country(cls,countries):

        cls.objects.filter(countries=countries).delete()
class Profile(models.Model):
    description = models.TextField(blank=True)
    username = models.ForeignKey(User,blank=True,on_delete=models.CASCADE)
    name =models.CharField(blank=True,max_length=100)
    email = models.EmailField(blank=True)
    avatar= ImageField(blank=True, manual_crop='800x800')
   
    def __str__(self):
        return self.name
class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    homepage = ImageField(blank=True, manual_crop='800x800')
    design = models.PositiveIntegerField(blank=True,default=0)
    usability = models.PositiveIntegerField(blank=True,default=0)
    creativity = models.PositiveIntegerField(blank=True,default=0)
    content = models.PositiveIntegerField(blank=True,default=0)
    overall_score = models.IntegerField(blank=True,default=0)
    username = models.ForeignKey(User,blank=True,on_delete=models.CASCADE)
   
   
    def __str__(self):
        return self.name
    
    @classmethod
    def get_all(cls):
        projects = Project.objects.all()
        return projects
class Rating(models.Model):
    design = models.IntegerField(blank=True,default=0)
    usability = models.IntegerField(blank=True,default=0)
    creativity = models.IntegerField(blank=True,default=0)
    content = models.IntegerField(blank=True,default=0)
    overall_score = models.IntegerField(blank=True,default=0)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
