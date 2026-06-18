from django.contrib import admin
from .models import category, Product, Order, Customer

admin.site.register(category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Customer)

