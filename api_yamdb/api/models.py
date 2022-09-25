from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.tokens import default_token_generator    


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
    role = models.CharField(max_length=80, null=True, blank=True, choices=ROLES)

@receiver(post_save, sender=User)
def post_save(sender, instanse, created, **kwargs):
    if created:
        confirmation_code = default_token_generator.make_token(
            instanse
        )
        instanse.confirmation_code = confirmation_code
        instanse.save()
    
