from django.contrib import admin
from .models import *
# Register your models 
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)