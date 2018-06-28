# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-03 00:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=255)),
                ('Lastname', models.CharField(max_length=255)),
                ('Dateofbirth', models.DateField()),
                ('Isorganizer', models.BooleanField(default=False)),
                ('Email', models.CharField(max_length=255)),
                ('Password', models.CharField(max_length=255)),
                ('Datejoined', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]