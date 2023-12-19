from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=200, unique=True)
    
    objects = UserManager()
    
    # Change The main Credential to be the 'email' instead of the 'username'
    username = None  # Set username to None to remove the field
    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = ['name']
    
    
