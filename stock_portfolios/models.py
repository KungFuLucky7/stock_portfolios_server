from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

class StockPortfolio(models.Model):
    """ The StockPortfolio model for the Stock Portfolios Server. """
    MODEL_CHOICES = (
        ('', ''),
        ('AAPL', 'AAPL'),
        ('GOOG', 'GOOG'),
        ('ORCL', 'ORCL'),
        ('HPQ', 'HPQ'),
        ('FB', 'FB'),
        ('YHOO', 'YHOO'),
    )
    symbol = models.CharField('Symbol', max_length=20, choices=MODEL_CHOICES, unique=True, default='')
    name = models.CharField('Name', max_length=200, blank=True, null=True)
    balance_status = models.BooleanField('Balance Status', default=True)
    change = models.FloatField('Change', blank=True, null=True, default=0.0)
    percent_change = models.CharField('Percent Change', max_length=200, blank=True, null=True, default='0.00%')
    user = models.ForeignKey(User, verbose_name='Stock Investor', editable=False)
    total_amount = models.FloatField('Total Amount', blank=True, null=True, default=100000.0)
    investment_amount = models.FloatField('Investment Amount', blank=True, null=True, default=0.0)
    quantity = models.IntegerField('Quantity', blank=True, null=True, default=0)
    earnings_losses = models.FloatField('Earnings/Loses', blank=True, null=True, default=0.0)
    timestamp = models.DateTimeField('Timestamp', auto_now_add=True)
    created_by = models.ForeignKey(User, verbose_name='Created By', related_name='%(app_label)s_created_by', blank=True, null=True, editable=False)
    modified_by = models.ForeignKey(User, verbose_name='Modified By', related_name='%(app_label)s_modified_by', blank=True, null=True, editable=False)
    modified_on = models.DateTimeField('Modified On', auto_now=True, blank=True, null=True, editable=False)
    previous_close = models.FloatField('Previous Close', blank=True, null=True, default=0.00)
    open = models.FloatField('Open', blank=True, null=True, default=0.0)
    bid = models.FloatField('Bid', blank=True, null=True, default=0.0)
    ask = models.FloatField('Ask', blank=True, null=True, default=0.0)
    one_yr_target_price = models.FloatField('One Year Target Price', blank=True, null=True, default=0.0)
    last_trade_date = models.CharField('Last Trade Date', max_length=200, blank=True, null=True)
    days_range = models.CharField('Days Range', max_length=200, blank=True, null=True)
    year_range = models.CharField('Year Range', max_length=200, blank=True, null=True)
    volume = models.IntegerField('Volume', blank=True, null=True, default=0)
    average_daily_volume = models.IntegerField('Average Daily Volume', blank=True, null=True, default=0)
    market_capitalization = models.CharField('Market Capitalization', max_length=200, blank=True, null=True)
    pe_ratio = models.FloatField('Price-Earnings Ratio', blank=True, null=True, default=0.0)
    earnings_share = models.FloatField('Earnings Share', blank=True, null=True, default=0.0)
    dividend_share = models.FloatField('Dividend Share', blank=True, null=True, default=0.0)
    dividend_yield = models.FloatField('Dividend Yield', blank=True, null=True, default=0.0)

    class Meta:
        verbose_name = 'Stock Portfolio'
        verbose_name_plural = 'Stock Portfolios'

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.symbol

    def was_added_recently(self):
        return self.timestamp >= timezone.now() - datetime.timedelta(days=1)
    was_added_recently.admin_order_field = 'timestamp'
    was_added_recently.boolean = True
    was_added_recently.short_description = 'Added recently?'
