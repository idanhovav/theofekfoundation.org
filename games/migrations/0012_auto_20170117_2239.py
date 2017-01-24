# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-18 06:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0011_gamesettings_difficulty'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamesettings',
            name='num_players',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='gamesettings',
            name='omniscient_view',
            field=models.NullBooleanField(),
        ),
    ]