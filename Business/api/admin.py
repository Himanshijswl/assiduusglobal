from django.contrib import admin
from .models import Product, Order, Line_Item

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'sku', 'name']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'datetime']


@admin.register(Line_Item)
class Line_ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'product', 'quantity']