# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-21 00:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_auto_20180509_0444'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Phonenumber',
            field=models.CharField(default=5555555555, max_length=10),
            preserve_default=False,
        ),
    ]