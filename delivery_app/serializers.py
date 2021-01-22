from rest_framework import serializers
from .models import Delivery_Partner,Vehicle_Class,Vehicle_Detail,Pending_Order,Delivery_Detail,Delivered_Order

#Serializers allow complex data such as querysets and model instances to be converted to native Python


#defining serializers for all models

class Delivery_Partner_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery_Partner
        fields = '__all__'

class Vehicle_Class_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle_Class
        fields = '__all__'

class Vehicle_Detail_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle_Detail
        fields = '__all__'

class Pending_Order_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Pending_Order
        fields = '__all__'

class Delivery_Detail_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery_Detail
        fields = '__all__'

class Delivered_Order_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Delivered_Order
        fields = '__all__'
