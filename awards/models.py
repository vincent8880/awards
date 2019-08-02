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
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
#     pic = ImageField(blank=True, manual_crop="")
#     bio = models.CharField(default="Hi!", max_length = 30)

#     @receiver(post_save, sender=User)
#     def create_user_profile(sender, instance, created, **kwargs):
#         if created:
#             Profile.objects.create(user=instance)

#     @receiver(post_save, sender=User)
#     def save_user_profile(sender, instance, **kwargs):
#         instance.profile.save()
    
#     @classmethod
#     def search_user(cls,name):
#         return User.objects.filter(username__icontains = name)
