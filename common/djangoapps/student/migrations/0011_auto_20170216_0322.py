# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_auto_20170213_0500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatereference',
            name='name',
            field=models.CharField(db_index=True, max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='candidatereference',
            name='phone_number',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='candidatereference',
            name='position',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
