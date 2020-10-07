from django.contrib import admin
from .models import Product, Customer, Order, Tag
# Register your models here.

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)
