# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0002_advert_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='pub_date',
            field=models.DateField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
