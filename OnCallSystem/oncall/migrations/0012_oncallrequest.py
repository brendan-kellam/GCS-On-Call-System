# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oncall', '0011_period'),
    ]

    operations = [
        migrations.CreateModel(
            name='OncallRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('week', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=500)),
                ('course', models.OneToOneField(default=None, to='oncall.Course')),
                ('coverage_teacher', models.OneToOneField(related_name='coverage_teacher', default=None, to='oncall.Teacher')),
                ('period', models.OneToOneField(default=None, to='oncall.Period')),
                ('request_teacher', models.OneToOneField(related_name='request_teacher', default=None, to='oncall.Teacher')),
                ('slot', models.OneToOneField(default=None, to='oncall.Slot')),
            ],
        ),
    ]
