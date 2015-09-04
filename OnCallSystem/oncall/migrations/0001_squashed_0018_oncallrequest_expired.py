# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    replaces = [(b'oncall', '0001_initial'), (b'oncall', '0002_slot_teacher'), (b'oncall', '0003_auto_20150714_1952'), (b'oncall', '0004_auto_20150714_1953'), (b'oncall', '0005_auto_20150714_1956'), (b'oncall', '0006_auto_20150719_1344'), (b'oncall', '0007_auto_20150719_1401'), (b'oncall', '0008_auto_20150719_1422'), (b'oncall', '0009_auto_20150719_1515'), (b'oncall', '0010_course'), (b'oncall', '0011_period'), (b'oncall', '0012_oncallrequest'), (b'oncall', '0013_auto_20150727_1954'), (b'oncall', '0014_auto_20150727_2002'), (b'oncall', '0015_auto_20150727_2014'), (b'oncall', '0016_auto_20150727_2107'), (b'oncall', '0017_oncallrequest_has_been_recived'), (b'oncall', '0018_oncallrequest_expired')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='oncall.Question'),
        ),
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
                ('oncall_count', models.IntegerField(default=0)),
                ('user', models.OneToOneField(default=None, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='slot',
            name='teachers',
            field=models.ManyToManyField(to=b'oncall.Teacher'),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_code', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('period_number', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='OncallRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('week', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=500)),
                ('course', models.ForeignKey(to='oncall.Course')),
                ('coverage_teacher', models.ForeignKey(related_name='coverage_teacher', to='oncall.Teacher')),
                ('period', models.ForeignKey(to='oncall.Period')),
                ('request_teacher', models.ForeignKey(related_name='request_teacher', to='oncall.Teacher')),
                ('slot', models.ForeignKey(to='oncall.Slot')),
                ('has_been_recived', models.BooleanField(default=False)),
                ('expired', models.BooleanField(default=False)),
            ],
        ),
    ]
