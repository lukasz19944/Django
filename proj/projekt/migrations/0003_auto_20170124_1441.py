# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projekt', '0002_zadanie_polecenie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=50)),
                ('nazwisko', models.CharField(max_length=50)),
                ('uczelnia', models.CharField(max_length=120)),
                ('kierunek', models.CharField(max_length=60)),
                ('telefon', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=40)),
                ('github', models.URLField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Zadanie',
        ),
    ]
