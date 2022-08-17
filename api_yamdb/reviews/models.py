from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MaxValueValidator
from django.utils import timezone

User = get_user_model()


class Categories(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название категории')
    slug = models.SlugField(max_length=50, unique=True, db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name} {self.name}'


class Genres(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Название жанра',
    )
    slug = models.SlugField(max_length=50, unique=True, db_index=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.slug


class Titles(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    year = models.IntegerField(
        validators=[MaxValueValidator(timezone.now().year)], verbose_name='Год'
    )
    description = models.CharField(
        max_length=255, null=True, blank=True, verbose_name='Описание'
    )
    genre = models.ManyToManyField(
        Genres,
        blank=True,
        related_name='genre',
        verbose_name='Жанр',
        db_index=True
    )
    category = models.ForeignKey(
        Categories,
        on_delete=models.SET_NULL,
        related_name='category',
        verbose_name='Категория',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name
