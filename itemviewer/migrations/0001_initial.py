# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_id', models.IntegerField(default=0)),
                ('item_name', models.CharField(default=b'', max_length=50)),
                ('icon_url', models.CharField(default=b'', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('match_type', models.CharField(default=b'Unknown', max_length=b'50')),
                ('match_id', models.IntegerField(default=0, unique=True)),
                ('match_duration', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('champion_id', models.IntegerField(default=0)),
                ('is_opponent', models.BooleanField(default=True)),
                ('match_won', models.BooleanField(default=False)),
                ('wards', models.IntegerField(default=0)),
                ('match', models.ForeignKey(to='itemviewer.Match')),
            ],
        ),
        migrations.CreateModel(
            name='Summoner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('summoner_name', models.CharField(default=b'', unique=True, max_length=50)),
                ('summoner_id', models.IntegerField(default=0, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='participant',
            name='summoner',
            field=models.ForeignKey(to='itemviewer.Summoner'),
        ),
        migrations.AddField(
            model_name='match',
            name='main_summoner',
            field=models.ForeignKey(to='itemviewer.Summoner'),
        ),
        migrations.AddField(
            model_name='item',
            name='participants',
            field=models.ManyToManyField(to='itemviewer.Participant'),
        ),
    ]
