from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    first_name = models.CharField('first name', max_length=150)
    last_name = models.CharField('last name', max_length=150)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta(AbstractUser.Meta):
        ordering = ['username']

    def __str__(self):
        return self.get_full_name()
