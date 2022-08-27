# Generated by Django 2.2.16 on 2022-08-27 20:32

from django.db import migrations, models

import reviews.validators


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20220828_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.PositiveSmallIntegerField(validators=[reviews.validators.year_validator], verbose_name='Год'),
        ),
    ]
