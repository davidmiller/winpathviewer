# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('winpathviewer', '0002_winpathresult'),
    ]

    operations = [
        migrations.AddField(
            model_name='winpathresult',
            name='visible_in_list',
            field=models.BooleanField(default=False),
        ),
    ]
