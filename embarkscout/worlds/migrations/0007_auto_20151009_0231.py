# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worlds', '0006_world_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='world',
            name='creature_seed',
            field=models.CharField(null=True, max_length=30),
        ),
        migrations.AddField(
            model_name='world',
            name='history_seed',
            field=models.CharField(null=True, max_length=30),
        ),
        migrations.AddField(
            model_name='world',
            name='name_seed',
            field=models.CharField(null=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='world',
            name='seed',
            field=models.CharField(null=True, max_length=30),
        ),
    ]
