from django.db import models
from django.contrib.auth.models import AbstractBaseUser

ROLE_CHOICES = (
    ('Admin', 'Admin'),
    ('Adept', 'Adept'),
    ('User', 'User'),
)


class User(AbstractBaseUser):
    username = models.CharField(
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(
        max_length=255,
    )
    last_name = models.CharField(
        max_length=255,
    )
    vk_id = models.CharField(
        max_length=20,
    )
    role = models.CharField(
        max_length=5,
        choices=ROLE_CHOICES,
        default='User',
    )
    about = models.TextField()
    picture = models.ImageField()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.vk_id
