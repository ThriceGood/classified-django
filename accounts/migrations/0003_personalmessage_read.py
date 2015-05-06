# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_personalmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalmessage',
            name='read',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
