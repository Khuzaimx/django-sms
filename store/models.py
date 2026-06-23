from django.db import models
import datetime

class category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"
class Customer(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    category=models.ForeignKey(category, on_delete=models.CASCADE, default=1)
    description=models.TextField(null=True, blank=True)
    image=models.ImageField(upload_to='uploads/products/')

    def __str__(self):
        return self.name


class Order(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=100)
    status=models.BooleanField(default=False)
    date=models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return f"{self.product.name} - {self.customer.first_name} {self.customer.last_name}"
# Create your models here.
