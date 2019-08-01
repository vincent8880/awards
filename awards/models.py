from django.db import models
from pyuploadcare.dj.models import ImageField

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    homepage = ImageField(blank=True, manual_crop='800x800')

    def __str__(self):
        return self.name
    
    @classmethod
    def get_all(cls):
        projects = Project.objects.all()
        return projects