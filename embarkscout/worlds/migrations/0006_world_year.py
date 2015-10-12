# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worlds', '0005_auto_20151008_0238'),
    ]

    operations = [
        migrations.AddField(
            model_name='world',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]
