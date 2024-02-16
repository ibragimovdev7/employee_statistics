from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser
import random
import string


def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

class CustomUserManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        user = self.model(phone=phone, **extra_fields)
        if not password:
            password = generate_random_password(10)
        user.set_password(password)
        user.is_superuser = False
        user.is_staff = False
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError("User must have a phone (number)")
        if not password:
            raise ValueError("User must have a password")
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    MALE = 'M'
    FEMALE = 'F'

    GENDERS = (
        (MALE, 'Erkak'),
        (FEMALE, 'Ayol')
    )
    phone = models.CharField(max_length=13,unique=True)
    # user's personal info
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=15, choices=GENDERS,
                              null=True, blank=True)
    birth_of_date = models.DateTimeField(auto_now_add=True)
    # Boolean fields to distinct users role
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.is_staff and self.is_active:
            return f'{self.phone} --- employee'
        if self.is_client and self.is_active:
            return f'{self.phone} --- client'
        if self.is_superuser:
            return self.phone

    USERNAME_FIELD = 'phone'
    objects = CustomUserManager()


