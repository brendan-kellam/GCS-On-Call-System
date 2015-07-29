# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oncall', '0005_auto_20150714_1956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='email_address',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='last_name',
        ),
        migrations.AddField(
            model_name='teacher',
            name='oncall_count',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='teacher',
            name='user',
            field=models.OneToOneField(default=None, to=settings.AUTH_USER_MODEL),
        ),
    ]
