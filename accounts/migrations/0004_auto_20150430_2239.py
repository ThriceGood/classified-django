# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_personalmessage_read'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='county',
            field=models.CharField(max_length=20, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='town',
            field=models.CharField(max_length=30, null=True),
            preserve_default=True,
        ),
    ]
