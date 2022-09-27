import datetime
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class User(AbstractUser):
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'
    ROLES = [
        ('admin', 'admin'),
        ('moderator', 'moderator'),
        ('user', 'user'),
    ]
    bio = models.TextField('Биография', null=True, blank=True)
    role = models.CharField(
        max_length=80, choices=ROLES, default='user'
    )
    confirmation_code = models.CharField(
        max_length=80, blank=True, default=""
    )

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_admin(self):
        return self.role == self.ADMIN


class Genre(models.Model):
    name = models.CharField(max_length=200, unique=True,
                            verbose_name='Жанр')
    slug = models.SlugField(unique=True, verbose_name='Адрес')

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True,
                            verbose_name='Название категории')
    slug = models.SlugField(unique=True, verbose_name='Адрес')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.TextField(
        'Наименование',
        help_text='Введите наименование'
    )
    year = models.IntegerField(
        default=current_year(),
        validators=[MinValueValidator(0), max_value_current_year]
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='title',
        blank=True,
        null=True,
        verbose_name='Категория',
        help_text='Категория, к которой будет относиться произведение'
    )
    genre = models.ManyToManyField(
        Genre,
        related_name='title',
        blank=True,
        null=True,
        verbose_name='Жанр',
        help_text='Жанр, к которой будет относиться произведение'
    )
    rating = models.IntegerField(
        default=10,
        validators=[MinValueValidator(1), MaxValueValidator(10)],
    )
    description = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def get_year(self):
        return self.year

    def __str__(self):
        return self.name[:10]


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    score = models.IntegerField(
        default=10,
        validators=[MinValueValidator(1), MaxValueValidator(10)],
    )
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'Обзор'
        verbose_name_plural = 'Обзоры'
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author'],
                name='unique_review'
            )
        ]

    def __str__(self):
        return self.text


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='сomments',
    )
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='сomments'
    )
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'

    def __str__(self):
        return self.text