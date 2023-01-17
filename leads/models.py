from django.db import models

from django.conf import settings

# from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

# SOURCE_CHOICES = [
#     ['yt', 'YoutTube'],
#     ['google', 'Google'],
#     ['newsletter', 'Newsletter'],
# ]

# class Agent(models.Model):
#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)

# User = get_user_model()


class User(AbstractUser):
    pass


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)

    # phone = models.BooleanField(default=False)
    # source = models.CharField(choices=SOURCE_CHOICES, max_length=100)

    # profile_picture = models.ImageField(blank=True, null=True)
    # special_files = models.FileField(blank=True, null=True)

    # agent = models.ForeignKey(Agent)
    # agent = models.ForeignKey('Agent', on_delete=models.SET_NULL, null=True)
    # agent = models.ForeignKey('Agent', on_delete=models.SET_DEFAULT, default=1)
    agent = models.ForeignKey('Agent', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Agent(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email
