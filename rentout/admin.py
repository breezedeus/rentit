from django.contrib import admin

# Register your models here.
from .models import Outorder, Wish


class WishAdmin(admin.ModelAdmin):
    model = Wish
    fieldsets = [
        ('Out-Order', {'fields': ['outorder']}),
        ('Creator Information', {'fields': ['creator', 'price', 'description', 'rating']}),
        ('Dates related to the wish', {'fields': ['start_date', 'end_date']}),
        ('Date that the wish was published', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ]
    list_display = ('id', 'creator', 'outorder', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['item']


class WishInline(admin.TabularInline):
    model = Wish
    extra = 0


class OutorderAdmin(admin.ModelAdmin):
    model = Outorder
    fieldsets = [
        ('Item for rent', {'fields': ['item_name', 'creator', 'address', 'price', 'description']}),
        ('Borrower', {'fields': ['borrower_id']}),
        ('Dates related to the wish', {'fields': ['start_date', 'end_date']}),
        ('Date that the order was published', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('id', 'item_name', 'available', 'creator', 'borrower_id', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['item_name']
    inlines = [WishInline]


admin.site.register(Outorder, OutorderAdmin)
admin.site.register(Wish, WishAdmin)
