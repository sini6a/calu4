# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-01 10:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20180228_1638'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='project',
            name='project_text',
            field=models.CharField(default='Default', max_length=1000),
            preserve_default=False,
        ),
    ]
