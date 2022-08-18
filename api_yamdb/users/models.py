from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    '''Пользовательские роли'''
    USER = 'User'
    MODERATOR = 'Moderator'
    ADMIN = 'Admin'
    ROLE = [
        (USER, 'User'),
        (MODERATOR, 'Moderator'),
        (ADMIN, 'Admin'),
    ]

    username = models.TextField('Имя пользователя', max_length=50,
                                unique=True)
    email = models.EmailField('Почта', unique=True)
    role = models.CharField('Роль пользователя',
                            choices=ROLE, default=USER)
    bio = models.TextField(verbose_name='О себе', null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    @property
    def is_user(self):
        '''Роли'''
        return self.role == self.USER

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_admin(self):
        return self.role == self.ADMIN