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
    bio = models.TextField('Биография', null=True, blank=True),
    role = models.CharField(
        max_length=80, null=True, blank=True, choices=ROLES
    ),
    confirmation_code = models.CharField(
        max_length=80, blank=True, default=""
    )


# class User(AbstractUser):
#     ADMIN = 'admin'
#     MODERATOR = 'moderator'
#     USER = 'user'
#     ROLES = [
#         (ADMIN, 'Administrator'),
#         (MODERATOR, 'Moderator'),
#         (USER, 'User'),
#     ]

#     # email = models.EmailField(
#     #     verbose_name='Адрес электронной почты',
#         # unique=True,
#     # )
#     # username = models.CharField(
#     #     verbose_name='Имя пользователя',
#     #     max_length=150,
#     #     null=True,
#     #     unique=True
#     # )
#     role = models.CharField(
#         verbose_name='Роль',
#         max_length=50,
#         choices=ROLES,
#         default=USER
#     )
#     bio = models.TextField(
#         verbose_name='О себе',
#         null=True,
#         blank=True
#     )

#     @property
#     def is_moderator(self):
#         return self.role == self.MODERATOR

#     @property
#     def is_admin(self):
#         return self.role == self.ADMIN

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']

#     class Meta:
#         ordering = ['id']
#         verbose_name = 'Пользователь'
#         verbose_name_plural = 'Пользователи'

#         constraints = [
#             models.CheckConstraint(
#                 check=~models.Q(username__iexact="me"),
#                 name="username_is_not_me"
#             )
#         ]
    
