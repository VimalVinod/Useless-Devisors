# forms.py
from django import forms
from .models import PetProfile

class PetProfileForm(forms.ModelForm):
    class Meta:
        model = PetProfile
        fields = ['name', 'bio', 'interests', 'profile_picture']
