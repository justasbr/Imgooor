# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gifai', '0002_gif_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gif',
            name='pub_date',
        ),
    ]
