# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oncall', '0003_auto_20150714_1952'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='slot',
            new_name='slots',
        ),
    ]
