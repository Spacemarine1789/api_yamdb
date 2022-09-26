from django.contrib.auth.models import AbstractUser
from django.db import models
 

class User(AbstractUser):
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'
    ROLES = [
        (ADMIN, 'Administrator'),
        (MODERATOR, 'Moderator'),
        (USER, 'User'),
    ]
    bio = models.TextField('Биография', null=True, blank=True),
    role = models.CharField(
        max_length=80, null=True, blank=True, choices=ROLES, default=USER
    ),
    confirmation_code = models.CharField(
        max_length=80, blank=True, default=""
    )

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_admin(self):
        return self.role == self.ADMIN
