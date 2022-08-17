from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Диспетчер пользовательских моделей пользователей, где email
    является уникальным идентификатором для аутинтификации всесто
    имен пользователей.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Создание и сохранение пользователя с указанным паролем и email.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Создание и сохранение суперпользователя с указанным паролем и email.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(
                _('Суперпользователь должен иметь атрибут is_staff=True.')
            )
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                _('Суперпользователь должен иметь атрибут is_superuser=True.')
            )
        return self.create_user(email, password, **extra_fields)
