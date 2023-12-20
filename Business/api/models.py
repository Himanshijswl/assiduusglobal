from django.db import models


class Product(models.Model):
    sku = models.IntegerField()
    name = models.CharField(max_length=50)
    
class Order(models.Model):
    datetime = models.DateTimeField(max_length=50)
    

class Line_Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    