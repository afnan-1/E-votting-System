from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserProfile(AbstractUser):
    picture = models.ImageField(null=True,blank=True)
    DEPARTMENTS = [
        ('CS', 'CS'),
        ('BBA', 'BBA'),
        ("HND","HND"),
        ("BTECH","BTECH"),
        ]
    department = models.CharField(choices=DEPARTMENTS,max_length=10,blank=True,null=True)

    def __str__(self):
        return self.username