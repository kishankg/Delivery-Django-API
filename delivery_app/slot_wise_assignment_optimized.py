from .models import Vehicle_Class, Vehicle_Detail, Delivery_Partner, Delivery_Detail
from django.db import connection
from .partner_vehicle_service import update_vehicle_availablity, update_drivers_availablity

def optimized_assignment_with_capacity(W, order_detail): 
    n = len(order_detail)
    K = [[0 for x in range(W + 1)] for x in range(n + 1)] 

    for i in range(n + 1): 
        wt = order_detail[i-1]['order_weight']
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif wt <= w: 
                K[i][w] = max(wt + K[i-1][w-wt],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 

    
    alloted_orders_ids = []
    alloted_order_weight = 0
    unalloted_order_detail = []
    i = n
    while i>0:
        if K[i][W] != K[i-1][W]:
            alloted_orders_ids.append(order_detail[i-1]['order_id'])
            alloted_order_weight += order_detail[i-1]['order_weight']
        else:
            unalloted_order_detail.append(order_detail[i-1])

        i = i-1

    return (alloted_orders_ids, alloted_order_weight, unalloted_order_detail)


def order_allotment(order_detail, slot):
    total_weight = 0
    for order in order_detail:
        total_weight += order['order_weight']

    vehicle_class_available = Vehicle_Class.objects.filter(**{slot: True}).order_by('-capacity')

    vechile_availability_detail = []

    with connection.cursor() as cursor:
        query = ("SELECT VD.registration_number, VC.vehicle_type, VC.capacity " +
            "FROM delivery_app_vehicle_detail as VD " + 
            "JOIN delivery_app_vehicle_class as VC " + 
            "on VC.vehicle_type=VD.vehicle_class_id " +
            "where VD.available = True and VC.{slot_name} = True " + 
            "order by VC.capacity DESC" ).format(slot_name=slot)
        # print(query)

        cursor.execute(query)
        vechile_availability_detail = cursor.fetchall()

    order_allotment_details = []
    unalloted_order_detail = order_detail
    for vehicle_details in vechile_availability_detail:
        (alloted_order_ids, alloted_order_weight, unalloted_order_detail) = optimized_assignment_with_capacity(vehicle_details[2],unalloted_order_detail)

        vehicle_alloted = Vehicle_Detail.objects.get(registration_number=vehicle_details[0])
        if vehicle_details[1] == 'Scooty' or vehicle_details[1] == 'Bike':
            driver_alloted = Delivery_Partner.objects.filter(available=True, two_wheeler=True).first()
        else:
            driver_alloted = Delivery_Partner.objects.filter(available=True, heavy_motor_vehicle=True).first()
        
        update_drivers_availablity(driver_alloted)
        update_vehicle_availablity(vehicle_alloted)

        order_allotment_details.append({"vehicle_type": vehicle_details[1], "vehicle_number": vehicle_details[0], "delivery_partner_id": driver_alloted.dl_number, "list_order_ids_assigned": alloted_order_ids})
        
        
        total_weight -= alloted_order_weight
        if total_weight <= 0:
            break

    return order_allotment_details