# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-04 03:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('game_name', models.CharField(max_length=128)),
                ('ai_turn', models.CharField(max_length=10)),
                ('monte_carlo_trials', models.IntegerField(null=True)),
                ('expansion_constant', models.DecimalField(decimal_places=10, max_digits=12, null=True)),
                ('certainty_threshold', models.DecimalField(decimal_places=3, max_digits=5, null=True)),
                ('time_to_think', models.DecimalField(decimal_places=4, max_digits=6, null=True)),
                ('anti', models.NullBooleanField()),
                ('ponder', models.NullBooleanField()),
                ('smart_simulation', models.NullBooleanField()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='gamesettings',
            unique_together=set([('id', 'game_name')]),
        ),
    ]