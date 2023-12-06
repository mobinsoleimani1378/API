from . import models
from django.contrib import admin


class OrderItemAdmin(admin.TabularInline):
    model = models.OrderItem


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_price',)
    inlines = (OrderItemAdmin,)
    list_filter = ('adress',)
