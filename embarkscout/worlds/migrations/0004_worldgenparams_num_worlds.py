# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worlds', '0003_worldgenparams_params'),
    ]

    operations = [
        migrations.AddField(
            model_name='worldgenparams',
            name='num_worlds',
            field=models.IntegerField(default=0),
        ),
    ]
