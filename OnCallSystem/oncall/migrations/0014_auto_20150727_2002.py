# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oncall', '0013_auto_20150727_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oncallrequest',
            name='coverage_teacher',
            field=models.OneToOneField(related_name='coverage_teacher', default=None, to='oncall.Teacher'),
        ),
        migrations.AlterField(
            model_name='oncallrequest',
            name='request_teacher',
            field=models.OneToOneField(related_name='request_teacher', default=None, to='oncall.Teacher'),
        ),
    ]
