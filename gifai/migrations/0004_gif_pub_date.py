# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gifai', '0003_remove_gif_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='gif',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now, auto_now_add=True),
            preserve_default=True,
        ),
    ]
