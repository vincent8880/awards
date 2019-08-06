from django.contrib import admin
from .models import Project,Profile, Rating, countries
# Register your models here.
admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(Rating)
admin.site.register(countries)

