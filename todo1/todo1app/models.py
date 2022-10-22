from django.db import models
from django.contrib.auth.models import AbstractUser

class UserForm(models.Model):
    name=models.CharField(max_length=150)
    username=models.CharField(max_length=150)
    Email=models.CharField(max_length=150)
    mobile=models.CharField(max_length=150)
    password=models.CharField(max_length=150)
    role=models.CharField(max_length=150)

    def __str__(self):
        return self.name
# Create your models here.

class Company(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    created_by=models.CharField(max_length=20)
    status=models.BooleanField(default=0)

    

    def __str__(self):
        return self.name

   
