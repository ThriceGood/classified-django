# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import adverts.models


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0006_advert_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='image',
            field=models.FileField(upload_to=adverts.models.get_upload_file_name, null=True, blank=True),
            preserve_default=True,
        ),
    ]
