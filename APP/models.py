from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    department_name=models.CharField(max_length=100,default=256)
    