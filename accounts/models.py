from django.db import models

class Customer(models.Model):
    cust_name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=12, null=True)
    email = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self) -> str:
        return self.cust_name
    
class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return self.name
    
class Product(models.Model):
    CATEGORY = (
        ('Indoor','Indoor'),
        ('Outdoor', 'Outdoor'),
    )
    product_name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.product_name
    
class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)