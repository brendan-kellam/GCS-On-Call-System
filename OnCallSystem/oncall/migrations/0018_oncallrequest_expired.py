# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oncall', '0017_oncallrequest_has_been_recived'),
    ]

    operations = [
        migrations.AddField(
            model_name='oncallrequest',
            name='expired',
            field=models.BooleanField(default=False),
        ),
    ]
