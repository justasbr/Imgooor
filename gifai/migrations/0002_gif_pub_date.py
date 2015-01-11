# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gifai', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gif',
            name='pub_date',
            field=models.DateTimeField(default=datetime.date(2014, 10, 18), auto_now_add=True),
            preserve_default=False,
        ),
    ]
