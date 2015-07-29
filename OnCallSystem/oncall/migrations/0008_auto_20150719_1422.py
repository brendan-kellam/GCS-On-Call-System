# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import annoying.fields


class Migration(migrations.Migration):

    dependencies = [
        ('oncall', '0007_auto_20150719_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='user',
            field=annoying.fields.AutoOneToOneField(default=None, to=settings.AUTH_USER_MODEL),
        ),
    ]
