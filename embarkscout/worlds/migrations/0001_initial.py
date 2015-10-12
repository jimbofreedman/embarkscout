# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='World',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('df_version', models.CharField(max_length=20)),
                ('es_version', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('name_english', models.CharField(max_length=80)),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WorldGenParams',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('df_version', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='world',
            name='world_gen_params',
            field=models.ForeignKey(to='worlds.WorldGenParams'),
        ),
    ]
