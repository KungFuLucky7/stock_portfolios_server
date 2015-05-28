# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_portfolios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockportfolio',
            name='symbol',
            field=models.CharField(default=b'', unique=True, max_length=20, verbose_name=b'Symbol', choices=[(b'', b''), (b'AAPL', b'AAPL'), (b'GOOG', b'GOOG'), (b'ORCL', b'ORCL'), (b'HPQ', b'HPQ'), (b'FB', b'FB'), (b'YHOO', b'YHOO')]),
        ),
    ]
