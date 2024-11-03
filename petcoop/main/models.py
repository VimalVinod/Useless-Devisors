from django.db import models
from django.contrib.auth.models import User

class PetProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    interests = models.TextField(blank=True, null=True)
    certificate_completed = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)  # Ensure this line is present

    def __str__(self):
        return self.name
