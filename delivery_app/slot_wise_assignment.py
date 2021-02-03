from .partner_vehicle_service import allot_bike,allot_scooty,allot_truck

def maxWeightAssignmentDP(W, order_detail): 
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

    
    orders_ids = []
    i = n
    while i>0:
        if K[i][W] != K[i-1][W]:
            orders_ids.append(order_detail[i-1]['order_id'])

        i = i-1

    return orders_ids
    

# We can club all three functions together in a single function
# From the function we would need slot information with order detail
# Call the "Vehicle Class List Model" to get vehicle class availability
# From the "Vehicle Detail List" filter using available vehicle class list


def first_slot_assignment(order_detail):
    total_weight = 0
    allotment_list = []
    first_dispatch_order_ids = []
    second_dispatch_order_ids = []
    first_dispatch_weight = 0
    second_dispatch_weight = 0

    # maxWeightAssignment(0,0,order_detail,[],0,first_dispatch_order_ids)
    first_dispatch_order_ids = maxWeightAssignmentDP(50,order_detail)

    for order in order_detail:
        total_weight += order['order_weight']
        if order['order_id'] in first_dispatch_order_ids:
            first_dispatch_weight += order['order_weight']
            continue
        second_dispatch_order_ids.append(order['order_id'])
    

    if first_dispatch_weight>0:
        if first_dispatch_weight<=30:
            allotment_list.append(allot_bike(first_dispatch_order_ids))
        else:
            allotment_list.append(allot_scooty(first_dispatch_order_ids))

    second_dispatch_weight = total_weight-first_dispatch_weight
    if second_dispatch_weight>0:
        if second_dispatch_weight<=30:
            allotment_list.append(allot_bike(second_dispatch_order_ids))
        else:
            allotment_list.append(allot_scooty(second_dispatch_order_ids))

    return allotment_list
    

# Vehicle availablity is same in both slots
def second_third_slot_assignment(order_detail):    
    total_weight = 0
    order_ids = []
    allotment_list = []
    for order in order_detail:
        total_weight += order['order_weight']
        order_ids.append(order['order_id'])
    
    if total_weight<=30:
        allotment_list.append(allot_bike(order_ids))
    elif total_weight<=50:
        allotment_list.append(allot_scooty(order_ids))
    else:
        allotment_list.append(allot_truck(order_ids))
    
    return allotment_list
        
def fourth_slot_assignment(order_detail):
    order_ids = []
    allotment_list = []

    for order in order_detail:
        order_ids.append(order['order_id'])
    
    allotment_list.append(allot_truck(order_ids))
    return allotment_list