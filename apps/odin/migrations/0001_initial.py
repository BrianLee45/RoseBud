# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 18:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loginReg', '0002_user_birthday'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=140)),
                ('eventDate', models.DateField(default=datetime.date.today)),
                ('eventTime', models.TimeField(default=datetime.date.today)),
                ('status', models.CharField(choices=[('Done', 'Done'), ('Missed', 'Missed'), ('Pending', 'Pending')], default='Pending', max_length=7)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='loginReg.User')),
            ],
        ),
    ]