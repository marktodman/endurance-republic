from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date', 'total',)

    fields = ('order_number', 'date', 'last_name', 'email', 'phone_number',
                'street_address1', 'town_or_city', 'county',
                'country', 'postcode', 'total',)

    list_display = ('order_number', 'date', 'last_name',
                    'total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
