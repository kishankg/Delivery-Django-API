from rest_framework import generics
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import Delivery_Partner_Serializer,Vehicle_Class_Serializer,Vehicle_Detail_Serializer,Pending_Order_Serializer,Delivery_Detail_Serializer,Delivered_Order_Serializer
from .models import Delivery_Partner,Vehicle_Class,Vehicle_Detail,Pending_Order,Delivery_Detail,Delivered_Order

#Declaration of all models viewset to do CRUD Operation

class Delivery_Partner_ViewSet(ModelViewSet):
    queryset = Delivery_Partner.objects.all()
    serializer_class = Delivery_Partner_Serializer

class Vehicle_Class_ViewSet(ModelViewSet):
    queryset = Vehicle_Class.objects.all()
    serializer_class = Vehicle_Class_Serializer

class Vehicle_Detail_ViewSet(ModelViewSet):
    queryset = Vehicle_Detail.objects.all()
    serializer_class = Vehicle_Detail_Serializer

class Pending_Order_ViewSet(ModelViewSet):
    queryset = Pending_Order.objects.all()
    serializer_class = Pending_Order_Serializer

class Delivery_Detail_ViewSet(ModelViewSet):
    queryset = Delivery_Detail.objects.all()
    serializer_class = Delivery_Detail_Serializer

class Delivered_Order_ViewSet(ModelViewSet):
    queryset = Delivered_Order.objects.all()
    serializer_class = Delivered_Order_Serializer