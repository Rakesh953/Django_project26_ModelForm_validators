# Generated by Django 5.0.6 on 2024-08-13 05:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(5)])),
                ('sid', models.IntegerField()),
                ('sage', models.IntegerField()),
                ('smobile', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('[6-9]\\d{9}')])),
            ],
        ),
    ]
