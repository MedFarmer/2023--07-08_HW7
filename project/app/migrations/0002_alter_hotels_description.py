# Generated by Django 4.2.3 on 2023-07-05 12:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotels',
            name='description',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(100)]),
        ),
    ]
