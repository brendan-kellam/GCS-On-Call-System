# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oncall', '0004_auto_20150714_1953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='slots',
        ),
        migrations.AddField(
            model_name='slot',
            name='teachers',
            field=models.ManyToManyField(to='oncall.Teacher'),
        ),
    ]
