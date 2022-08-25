# Generated by Django 2.2.16 on 2022-08-25 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220825_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('user', 'user'), ('moderator', 'moderator'), ('admin', 'admin')], default='user', max_length=100, verbose_name='Роль пользователя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.TextField(max_length=50, unique=True, verbose_name='Имя пользователя'),
        ),
    ]
