from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    full_name = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to = "profile_image/", blank = True, null = True)

    def __str__(self):
        return f"{self.username}"
