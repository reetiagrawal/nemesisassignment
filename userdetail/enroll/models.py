from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class FullDetail(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE)
     address = models.CharField(max_length=100)

     def __str__(self):
          return self.user.username


class User(models.Model):
     username = models.CharField(max_length=50)
     email = models.EmailField(max_length=50)


