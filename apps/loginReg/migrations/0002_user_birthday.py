# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 18:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginReg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(default=datetime.date.today),
        ),
    ]