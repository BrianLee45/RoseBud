# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 03:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('odin', '0002_auto_20170426_1214'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='event',
            unique_together=set([('eventDate', 'eventTime')]),
        ),
    ]
