# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worlds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worldgenparams',
            name='df_version',
            field=models.CharField(max_length=20, default='0.40.24'),
        ),
    ]
