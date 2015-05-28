from django.contrib import admin
from stock_portfolios.models import StockPortfolio

class StockPortfolioAdmin(admin.ModelAdmin):
    """ Administrative interface for the StockPortfolio model """
    fieldsets = [
        ('Stock Name & Status', {
            'fields': ('symbol', 'name', 'balance_status', 'change', 'percent_change')
        }),
        ('Investment Information', {
            'fields': ('total_amount', 'investment_amount', 'quantity', 'earnings_losses')
        }),
        (None, {
            'fields': ('timestamp', 'created_by', 'modified_by', 'modified_on')
        }),
        ('Stock Detailed Information', {
            'classes': ('extrapretty',),
            'fields': ('previous_close', 'open', 'bid', 'ask', 'one_yr_target_price', 
                       'last_trade_date', 'days_range', 'year_range', 'volume', 'average_daily_volume', 
                       'market_capitalization', 'pe_ratio', 'earnings_share', 'dividend_share', 'dividend_yield')
        }),
    ]
    readonly_fields=('timestamp', 'created_by', 'modified_by', 'modified_on')
    list_display = ('symbol', 'name', 'balance_status', 'change', 'percent_change', 'user', 'timestamp', 'total_amount', 'investment_amount', 'was_added_recently')
    list_filter = ('symbol', 'name', 'created_by', 'modified_by', 'modified_on')
    search_fields = ('symbol', 'name')
    date_hierarchy = 'timestamp'
    ordering = ['symbol']

    def save_model(self, request, obj, form, change):
        if obj.pk is None:
            obj.user = request.user
            obj.created_by = request.user
        obj.modified_by = request.user
        obj.save()

admin.site.register(StockPortfolio, StockPortfolioAdmin)
