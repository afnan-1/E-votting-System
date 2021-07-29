from django.db import models
from django.utils import tree

# Create your models here.
class Societie(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.name

class SocietyCandidate(models.Model):
    society = models.ForeignKey(Societie,on_delete=models.CASCADE,related_name='society')
    member_name = models.CharField(max_length=100,null=True,blank=True)
    votes = models.IntegerField(default=0)
    image = models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.member_name



class StudentUserName(models.Model):
    candidate = models.ForeignKey(SocietyCandidate,on_delete=models.DO_NOTHING,related_name="candidate")
    username = models.CharField(max_length=20)

    def __str__(self):
        return self.username