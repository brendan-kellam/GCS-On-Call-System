# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oncall', '0018_oncallrequest_expired'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
