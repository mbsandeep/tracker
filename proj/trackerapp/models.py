# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class AppUser(AbstractUser):
    GENDERS = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
    )
    gender = models.CharField(
        max_length=6,
        choices=GENDERS,
        blank=True,
        null=True,
        default='MALE',
    )
    dob = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'auth_user'


class UserLocation(models.Model):
    id = models.BigAutoField(primary_key='true')
    location = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    loctime = models.DateTimeField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
