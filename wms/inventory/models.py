from django.db import models
from product.models import Product, Shipment, Stock, Supplier
from warehouse.models import User, Category, Warehouse

# Create your models here.

class Order(models.Model):
    order_number = models.CharField(max_length=255, unique=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=250)
    order_date = models.DateField(auto_now_add=True)
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    ordered_products = models.ManyToManyField(Product)

    def __str__(self):
        return f'Order {self.order_number}'

class InventoryMovement(models.Model):
    MOVEMENT_TYPE_CHOICES = [
        ('in', 'In'),
        ('out', 'Out'),
        ('transfer', 'Transfer'),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    movement_type = models.CharField(max_length=225, choices=MOVEMENT_TYPE_CHOICES)

    def __str__(self):
        return f'{self.movement_type} {self.product.name} in {self.warehouse.name}'
