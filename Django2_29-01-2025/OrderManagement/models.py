from django.db import models
from CRUD_APP.models import *

# Create your models here.
class Customer(models.Model):
    customer_name = models.CharField(max_length=200, null=True)
    customer_since = models.DateTimeField(auto_now_add=True)#models.DateField(null=True)
    
    def __str__(self):

        return self.customer_name
    
class Orders(models.Model):

    customer_reference = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    product_reference = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True)
    order_number = models.CharField(max_length=20,null=True)
    order_date = models.DateTimeField(auto_now_add=True,)
    quantity = models.FloatField(default=0)
    amount = models.FloatField(default=0)
    gst_amount = models.FloatField(default=0)
    bill_amount = models.FloatField(default=0)

    def __str__(self):
        return self.order_number