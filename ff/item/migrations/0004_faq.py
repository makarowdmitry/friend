# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_auto_20150627_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=1250, verbose_name=b'\xd0\x92\xd0\xbe\xd0\xbf\xd1\x80\xd0\xbe\xd1\x81')),
                ('answer', models.CharField(max_length=2250, verbose_name=b'\xd0\xbe\xd1\x82\xd0\xb2\xd0\xb5\xd1\x82')),
            ],
            options={
                'verbose_name': '\u0412\u043e\u043f\u0440\u043e\u0441',
                'verbose_name_plural': '\u0412\u043e\u043f\u0440\u043e\u0441',
            },
        ),
    ]
