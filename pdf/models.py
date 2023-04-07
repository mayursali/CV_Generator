from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    summary= models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    experience = models.CharField(max_length=200)
    skills = models.CharField(max_length=200)