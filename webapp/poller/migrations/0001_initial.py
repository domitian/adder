# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-03 10:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'Queued'), (1, 'Finished')], default=0)),
                ('inp', models.CharField(max_length=200)),
                ('result', models.CharField(max_length=200)),
            ],
        ),
    ]