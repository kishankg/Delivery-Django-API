from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from .assignment_service import partner_assignment
from django.views.decorators.http import require_http_methods


# Process request and Call to assignment service
@require_http_methods(["POST"])
def delivery_assignment(request):
    total_order=json.loads(request.body)
    response = []

    # First we will call the service to append order details in Pending Order List Model

    # Slot wise processing
    for slot in range(4):
        response.append(partner_assignment(total_order[slot],slot+1))

    return JsonResponse({"data": response})

    #Update Delivered Order List Model after delivery

