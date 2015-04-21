# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itemviewer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('match_id', models.IntegerField(default=0, unique=True)),
                ('match_won', models.BooleanField(default=False)),
                ('champion', models.IntegerField(default=0)),
                ('item0', models.IntegerField(null=True)),
                ('item1', models.IntegerField(null=True)),
                ('item2', models.IntegerField(null=True)),
                ('item3', models.IntegerField(null=True)),
                ('item4', models.IntegerField(null=True)),
                ('item5', models.IntegerField(null=True)),
                ('item6', models.IntegerField(null=True)),
                ('wards', models.IntegerField(default=0)),
                ('vision_wards', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='summoner',
            name='summoner_id',
            field=models.IntegerField(default=0, unique=True),
        ),
        migrations.AlterField(
            model_name='summoner',
            name='summoner_name',
            field=models.CharField(default=b'', unique=True, max_length=50),
        ),
        migrations.AddField(
            model_name='match',
            name='summoner',
            field=models.ForeignKey(to='itemviewer.Summoner'),
        ),
    ]
