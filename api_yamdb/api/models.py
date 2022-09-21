from django.contrib.auth.models import AbstractUser
from django.db import models


ROLES = (
    ('user', 'Пользователь'),
    ('admin','Админ'),
    ('moderator','Модератор'),
)

class User(AbstractUser):
    bio = models.TextField(
        'Биография',
        blank=True,
    ),
    role = models.CharField(max_length=80, choices=ROLES)
