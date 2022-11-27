# Generated by Django 4.1.3 on 2022-11-15 16:23

from django.db import migrations, models
import reviews.validators


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_alter_title_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.PositiveSmallIntegerField(validators=[reviews.validators.year_validator], verbose_name='Год'),
        ),
    ]
