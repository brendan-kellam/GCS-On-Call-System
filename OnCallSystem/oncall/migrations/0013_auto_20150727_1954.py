# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('oncall', '0012_oncallrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oncallrequest',
            name='coverage_teacher',
            field=models.OneToOneField(related_name='coverage_teacher', default=uuid.uuid4, to='oncall.Teacher'),
        ),
        migrations.AlterField(
            model_name='oncallrequest',
            name='request_teacher',
            field=models.OneToOneField(related_name='request_teacher', default=uuid.uuid4, to='oncall.Teacher'),
        ),
    ]
