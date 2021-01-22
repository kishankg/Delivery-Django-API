from django.db import models

# Delivery Partner
class Delivery_Partner(models.Model):
    dl_number = models.CharField(max_length=16,primary_key=True)
    name = 	models.CharField(max_length=30,blank=False)
    contact = models.IntegerField(blank=False)
    email = models.EmailField(blank=False)
    available = models.BooleanField(default=True)
    two_wheeler = models.BooleanField(default=False)
    heavy_motor_vehicle = models.BooleanField(default=False)
 
    def __str__(self):
        return self.name


# Vehicle Class
class Vehicle_Class(models.Model):
    vehicle_type = 	models.CharField(max_length=30,blank=False,primary_key=True)
    capacity = models.IntegerField(blank=False)
    first_slot = models.BooleanField(default=False)
    second_slot = models.BooleanField(default=False)
    third_slot = models.BooleanField(default=False)
    fourth_slot = models.BooleanField(default=False)
 
    def __str__(self):
        return self.vehicle_type

# Vehicle Class
class Vehicle_Detail(models.Model):
    registration_number = models.CharField(max_length=10,primary_key=True)
    vehicle_class = models.ForeignKey(Vehicle_Class,on_delete=models.CASCADE,blank=False)
    available = models.BooleanField(default=True)
 
    def __str__(self):
        return self.registration_number

# Pending Order
class Pending_Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    weight = models.IntegerField(blank=False)
    slot_number = models.IntegerField(blank=False)
    # customer_id = models.ForeignKey(Customer)
    delivery_address = models.CharField(max_length=40,blank=False)
    delivery_status_code = models.IntegerField(blank=False)

    def __str__(self):
        return self.order_id

# Delivery Detail
class Delivery_Detail(models.Model):
    delivery_id = models.AutoField(primary_key=True)
    partner_id = models.ForeignKey(Delivery_Partner,on_delete=models.PROTECT)
    vehicle_id = models.ForeignKey(Vehicle_Detail,on_delete=models.CASCADE,default="null")
    order_id = models.ForeignKey(Pending_Order,on_delete=models.CASCADE)
    delivery_status_code = models.IntegerField(blank=False)
 
    def __str__(self):
        return self.delivery_id

# Delivered Order
class Delivered_Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    weight = models.IntegerField(blank=False)
    slot_number = models.IntegerField(blank=False)
    # customer_id = models.ForeignKey(Customer)
    delivery_address = models.CharField(max_length=40,blank=False)
    delivery_detail_id = models.ForeignKey(Delivery_Detail,on_delete=models.CASCADE)
    delivery_feedback =  models.CharField(max_length=100)

    def __str__(self):
        return self.order_id
