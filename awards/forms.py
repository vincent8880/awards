from django import forms
from .models import Project,Profile,Rating

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['username',]

class RatingForm(forms.ModelForm):
    class Meta:
        model=Rating
        exclude=['overall_score','profile','project']
class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        exclude=['username','design','usability','creativity','content','overall_score','profile',]
        