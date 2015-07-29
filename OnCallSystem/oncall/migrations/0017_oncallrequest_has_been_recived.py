# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oncall', '0016_auto_20150727_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='oncallrequest',
            name='has_been_recived',
            field=models.BooleanField(default=False),
        ),
    ]
