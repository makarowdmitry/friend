# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_auto_20150729_0700'),
    ]

    operations = [
        migrations.CreateModel(
            name='Securecode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=250, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xb4')),
            ],
            options={
                'verbose_name': '\u041a\u043e\u0434',
                'verbose_name_plural': '\u041a\u043e\u0434\u044b',
            },
        ),
    ]
