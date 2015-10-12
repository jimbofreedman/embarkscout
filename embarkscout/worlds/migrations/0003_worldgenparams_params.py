# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worlds', '0002_auto_20151008_0218'),
    ]

    operations = [
        migrations.AddField(
            model_name='worldgenparams',
            name='params',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
