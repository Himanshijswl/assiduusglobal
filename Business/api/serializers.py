from rest_framework import serializers
from .models import Product, Order, Line_Item


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'sku', 'name']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'datetime']


class Line_ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Line_Item
        fields = ['id', 'order', 'product', 'quantity']