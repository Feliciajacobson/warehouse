from django.db import models
import uuid
from warehouse.models import User, Warehouse, Category

# from django.core.mail import send_mail
# from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=250)
    sku = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    description = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)  # Use DecimalField for price

    def __str__(self):
        return self.name

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    reorder_level = models.IntegerField()

    def __str__(self):
        return f'{self.product.name} in {self.warehouse.name}'
    
#     reorder_level = models.IntegerField()

#     def check_reorder(self):
#         if self.quantity < self.reorder_level:
#             self.send_alert()

#     def send_alert(self):
#         subject = f"Stock Alert: {self.product.name}"
#         message = f"The stock for {self.product.name} is below the reorder level. Current quantity: {self.quantity}. Please reorder!"
#         recipients = ['manager@example.com']  # Replace with your manager's email or fetch dynamically
#         send_mail(subject, message, 'from@example.com', recipients)

# # Signal to check reorder after saving Stock
# @receiver(post_save, sender=Stock)
# def check_stock_reorder(sender, instance, created, **kwargs):
#     if not created:  # Only check on updates, not on creation
#         instance.check_reorder()

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    products_supplied = models.ManyToManyField(Product)

    def __str__(self):
        return self.name

class Shipment(models.Model):
    shipment_number = models.CharField(max_length=255, unique=True)
    carrier = models.CharField(max_length=255)
    shipping_address = models.CharField(max_length=255)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    shipment_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateField()
    products = models.ManyToManyField(Product)  # A shipment can have multiple products

    def __str__(self):
        return f'Shipment {self.shipment_number}'
