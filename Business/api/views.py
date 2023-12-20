from django.shortcuts import render
from rest_framework.response import Response
from .models import Product, Order, Line_Item
from .serializers import ProductSerializer, OrderSerializer, Line_ItemSerializer
from rest_framework import status
from rest_framework import viewsets


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

class OrderModelViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

class Line_ItemModelViewSet(viewsets.ModelViewSet):
    queryset = Line_Item.objects.all()
    serializer_class = Line_ItemSerializer
    
