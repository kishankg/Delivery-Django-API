from django.conf.urls import include,url
from delivery_app import rest_views
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register("deliverypartner",rest_views.Delivery_Partner_ViewSet,basename="deliverypartner")
router.register("vehicleclass",rest_views.Vehicle_Class_ViewSet,basename="vehicleclass")
router.register("vehicledetail",rest_views.Vehicle_Detail_ViewSet,basename="vehicledetail")
router.register("pendingorder",rest_views.Pending_Order_ViewSet,basename="pendingorder")
router.register("deliverydetail",rest_views.Delivery_Detail_ViewSet,basename="deliverydetail")
router.register("deliveredorder",rest_views.Delivered_Order_ViewSet,basename="deliveredorder")

urlpatterns = router.urls