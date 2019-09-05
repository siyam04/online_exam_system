from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    profile_name = models.CharField(max_length=250, blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    class Meta:
        verbose_name_plural = 'User Profiles'

    def __str__(self):
        return self.user.username
