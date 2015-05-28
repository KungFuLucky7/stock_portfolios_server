# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StockPortfolio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('symbol', models.CharField(default=b'', unique=True, max_length=20, verbose_name=b'Symbol', choices=[(b'', b''), (b'AAPL', b'AAPL'), (b'GOOG', b'GOOG'), (b'HPQ', b'HPQ')])),
                ('name', models.CharField(max_length=200, null=True, verbose_name=b'Name', blank=True)),
                ('balance_status', models.BooleanField(default=True, verbose_name=b'Balance Status')),
                ('change', models.FloatField(default=0.0, null=True, verbose_name=b'Change', blank=True)),
                ('percent_change', models.CharField(default=b'0.00%', max_length=200, null=True, verbose_name=b'Percent Change', blank=True)),
                ('total_amount', models.FloatField(default=100000.0, null=True, verbose_name=b'Total Amount', blank=True)),
                ('investment_amount', models.FloatField(default=0.0, null=True, verbose_name=b'Investment Amount', blank=True)),
                ('quantity', models.IntegerField(default=0, null=True, verbose_name=b'Quantity', blank=True)),
                ('earnings_losses', models.FloatField(default=0.0, null=True, verbose_name=b'Earnings/Loses', blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name=b'Timestamp')),
                ('modified_on', models.DateTimeField(auto_now=True, verbose_name=b'Modified On', null=True)),
                ('previous_close', models.FloatField(default=0.0, null=True, verbose_name=b'Previous Close', blank=True)),
                ('open', models.FloatField(default=0.0, null=True, verbose_name=b'Open', blank=True)),
                ('bid', models.FloatField(default=0.0, null=True, verbose_name=b'Bid', blank=True)),
                ('ask', models.FloatField(default=0.0, null=True, verbose_name=b'Ask', blank=True)),
                ('one_yr_target_price', models.FloatField(default=0.0, null=True, verbose_name=b'One Year Target Price', blank=True)),
                ('last_trade_date', models.CharField(max_length=200, null=True, verbose_name=b'Last Trade Date', blank=True)),
                ('days_range', models.CharField(max_length=200, null=True, verbose_name=b'Days Range', blank=True)),
                ('year_range', models.CharField(max_length=200, null=True, verbose_name=b'Year Range', blank=True)),
                ('volume', models.IntegerField(default=0, null=True, verbose_name=b'Volume', blank=True)),
                ('average_daily_volume', models.IntegerField(default=0, null=True, verbose_name=b'Average Daily Volume', blank=True)),
                ('market_capitalization', models.CharField(max_length=200, null=True, verbose_name=b'Market Capitalization', blank=True)),
                ('pe_ratio', models.FloatField(default=0.0, null=True, verbose_name=b'Price-Earnings Ratio', blank=True)),
                ('earnings_share', models.FloatField(default=0.0, null=True, verbose_name=b'Earnings Share', blank=True)),
                ('dividend_share', models.FloatField(default=0.0, null=True, verbose_name=b'Dividend Share', blank=True)),
                ('dividend_yield', models.FloatField(default=0.0, null=True, verbose_name=b'Dividend Yield', blank=True)),
                ('created_by', models.ForeignKey(related_name='stock_portfolios_created_by', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name=b'Created By')),
                ('modified_by', models.ForeignKey(related_name='stock_portfolios_modified_by', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name=b'Modified By')),
                ('user', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL, verbose_name=b'Stock Investor')),
            ],
            options={
                'verbose_name': 'Stock Portfolio',
                'verbose_name_plural': 'Stock Portfolios',
            },
        ),
    ]
