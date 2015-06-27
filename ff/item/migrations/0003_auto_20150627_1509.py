# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_auto_20150627_1459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='good',
            name='name',
        ),
        migrations.AlterField(
            model_name='good',
            name='link',
            field=models.CharField(max_length=1250, verbose_name=b'\xd0\xa1\xd1\x81\xd1\x8b\xd0\xbb\xd0\xba\xd0\xb0 \xd0\xaf\xd0\xbd\xd0\xb4\xd0\xb5\xd0\xba\xd1\x81 \xd0\xbc\xd0\xb0\xd1\x80\xd0\xba\xd0\xb5\xd1\x82\xd0\xb0', blank=True),
        ),
    ]
