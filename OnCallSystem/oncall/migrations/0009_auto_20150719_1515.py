# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('oncall', '0008_auto_20150719_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='user',
            field=models.OneToOneField(default=None, to=settings.AUTH_USER_MODEL),
        ),
    ]
