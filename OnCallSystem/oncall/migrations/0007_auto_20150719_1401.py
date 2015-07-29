# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oncall', '0006_auto_20150719_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='oncall_count',
            field=models.IntegerField(default=0),
        ),
    ]
