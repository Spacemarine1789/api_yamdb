from django.db import models


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
        ordering = ('-name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.TextField(
        'Наименование',
        help_text='Введите наименование'
    )
    year = models.DateTimeField(
        'Год публикации',
        auto_now_add=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
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

    class Meta:
        ordering = ('-year',)
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def get_year(self):
        return self.year.year

    def __str__(self):
        return self.name[:10]
