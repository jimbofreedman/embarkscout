# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worlds', '0004_worldgenparams_num_worlds'),
    ]

    operations = [
        migrations.AddField(
            model_name='world',
            name='seed',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='world',
            name='es_version',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='world',
            name='height',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='world',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='world',
            name='name_english',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='world',
            name='width',
            field=models.IntegerField(null=True),
        ),
    ]
