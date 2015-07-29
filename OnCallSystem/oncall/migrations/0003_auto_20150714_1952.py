# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oncall', '0002_slot_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='slot',
        ),
        migrations.AddField(
            model_name='teacher',
            name='slot',
            field=models.ManyToManyField(to='oncall.Slot'),
        ),
    ]
