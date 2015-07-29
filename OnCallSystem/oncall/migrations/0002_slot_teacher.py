# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oncall', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slot_id', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email_address', models.EmailField(max_length=254)),
                ('slot', models.ForeignKey(default=None, to='oncall.Slot')),
            ],
        ),
    ]
