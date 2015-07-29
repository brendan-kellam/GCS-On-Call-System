# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oncall', '0015_auto_20150727_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oncallrequest',
            name='course',
            field=models.ForeignKey(to='oncall.Course'),
        ),
        migrations.AlterField(
            model_name='oncallrequest',
            name='coverage_teacher',
            field=models.ForeignKey(related_name='coverage_teacher', to='oncall.Teacher'),
        ),
        migrations.AlterField(
            model_name='oncallrequest',
            name='period',
            field=models.ForeignKey(to='oncall.Period'),
        ),
        migrations.AlterField(
            model_name='oncallrequest',
            name='request_teacher',
            field=models.ForeignKey(related_name='request_teacher', to='oncall.Teacher'),
        ),
        migrations.AlterField(
            model_name='oncallrequest',
            name='slot',
            field=models.ForeignKey(to='oncall.Slot'),
        ),
    ]
