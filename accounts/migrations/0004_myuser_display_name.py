# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 22:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20170611_0532'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='display_name',
            field=models.CharField(default='', max_length=40),
        ),
    ]
