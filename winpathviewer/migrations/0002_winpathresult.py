# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import opal.models


class Migration(migrations.Migration):

    dependencies = [
        ('opal', '0010_auto_20160227_2227'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('winpathviewer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WinPathResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('lab_number', models.CharField(max_length=200, null=True, blank=True)),
                ('profile_code', models.CharField(max_length=200, null=True, blank=True)),
                ('profile_description', models.CharField(max_length=200, null=True, blank=True)),
                ('request_datetime', models.DateTimeField(null=True, blank=True)),
                ('observation_datetime', models.DateTimeField(null=True, blank=True)),
                ('last_edited', models.DateTimeField(null=True, blank=True)),
                ('result_status', models.CharField(max_length=200, null=True, blank=True)),
                ('observations', models.TextField(null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='created_winpathviewer_winpathresult_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('episode', models.ForeignKey(to='opal.Episode')),
                ('updated_by', models.ForeignKey(related_name='updated_winpathviewer_winpathresult_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, models.Model),
        ),
    ]
