# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-29 01:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 29, 1, 48, 0, 667632, tzinfo=utc)),
        ),
    ]
