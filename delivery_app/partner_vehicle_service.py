from .models import Vehicle_Class, Vehicle_Detail, Delivery_Partner, Delivery_Detail
from .serializers import Vehicle_Class_Serializer,Vehicle_Detail_Serializer, Delivery_Partner_Serializer

# There would be a service to update delivery partners availablity
def make_all_drivers_available():
    Delivery_Partner.objects.all().update(available=True)

def make_all_vehicles_available():
    Vehicle_Detail.objects.all().update(available=True)

def update_vehicle_availablity(vehicle_alloted):
    vehicle_alloted.available = False
    vehicle_alloted.save()

def update_drivers_availablity(driver_alloted):
    driver_alloted.available = False
    driver_alloted.save()

# Call this function after every allotment
def store_delivery_detail(vehicle_alloted,driver_alloted,order_ids):
    for order_id in order_ids:
        delivery_detail = Delivery_Detail(vehicle_id=vehicle_alloted.registration_number,partner_id=driver_alloted.dl_number,order_ids=order_id)
        delivery_detail.save()

def allot_scooty(order_ids):
    vehicle_alloted = Vehicle_Detail.objects.filter(vehicle_class='Scooty',available=True)[:1].get()
    driver_alloted = Delivery_Partner.objects.filter(two_wheeler=True,available=True)[:1].get()
    update_vehicle_availablity(vehicle_alloted)
    update_drivers_availablity(driver_alloted)
    return ({"vehicle_type": "scooty", "vehicle_number": vehicle_alloted.registration_number, "delivery_partner_id": driver_alloted.dl_number, "list_order_ids_assigned": order_ids})

def allot_bike(order_ids):
    vehicle_alloted = Vehicle_Detail.objects.filter(vehicle_class='Bike',available=True)[:1].get()
    driver_alloted = Delivery_Partner.objects.filter(two_wheeler=True,available=True)[:1].get()
    update_vehicle_availablity(vehicle_alloted)
    update_drivers_availablity(driver_alloted)
    return ({"vehicle_type": "bike", "vehicle_number": vehicle_alloted.registration_number, "delivery_partner_id": driver_alloted.dl_number, "list_order_ids_assigned": order_ids})

def allot_truck(order_ids):
    vehicle_alloted = Vehicle_Detail.objects.filter(vehicle_class='Truck',available=True)[:1].get()
    driver_alloted = Delivery_Partner.objects.filter(heavy_motor_vehicle=True,available=True)[:1].get()
    update_vehicle_availablity(vehicle_alloted)
    update_drivers_availablity(driver_alloted)
    return ({"vehicle_type": "truck", "vehicle_number": vehicle_alloted.registration_number, "delivery_partner_id": driver_alloted.dl_number, "list_order_ids_assigned": order_ids})

