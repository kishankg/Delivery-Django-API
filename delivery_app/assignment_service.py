from .partner_vehicle_service import make_all_drivers_available,make_all_vehicles_available
from .slot_wise_assignment import first_slot_assignment, second_third_slot_assignment, fourth_slot_assignment
from .slot_wise_assignment_optimized import order_allotment

slot_dict = {1: "first_slot", 2: "second_slot", 3: "third_slot", 4: "fourth_slot"}

def partner_assignment(order_detail, slot):
    #If there is no order send empty list
    if len(order_detail) == 0:
        return []

    # There would be a service to update drivers and vehicles detail before/after every slot
    make_all_drivers_available()
    make_all_vehicles_available()

    print(order_allotment(order_detail,slot_dict.get(slot)))

    make_all_drivers_available()
    make_all_vehicles_available()

    # slot wise assignment
    if slot==1:
        return first_slot_assignment(order_detail)
    if slot==2 or slot==3:
        return second_third_slot_assignment(order_detail)
    else:
        return fourth_slot_assignment(order_detail)