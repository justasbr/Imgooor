# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('gifai', '0007_auto_20141018_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gif',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 18, 21, 23, 30, 973356), auto_now_add=True),
        ),
    ]
