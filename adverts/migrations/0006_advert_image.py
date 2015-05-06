# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import adverts.models


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0005_auto_20150416_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='image',
            field=models.FileField(null=True, upload_to=adverts.models.get_upload_file_name),
            preserve_default=True,
        ),
    ]
