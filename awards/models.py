from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    homepage = models.URLField(blank=True)

    def __str__(self):
        return self.name
    
    @classmethod
    def get_all(cls):
        projects = Project.objects.all()
        return projects