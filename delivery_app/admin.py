from django.contrib import admin
from .models import Delivery_Partner,Vehicle_Class,Vehicle_Detail,Pending_Order,Delivery_Detail,Delivered_Order

# Register your models here.
admin.site.register(Delivery_Partner)
admin.site.register(Vehicle_Class)
admin.site.register(Vehicle_Detail)
admin.site.register(Pending_Order)
admin.site.register(Delivery_Detail)
admin.site.register(Delivered_Order)
