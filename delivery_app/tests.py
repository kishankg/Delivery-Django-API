from django.test import TestCase, Client
from .models import Delivery_Partner,Vehicle_Class,Vehicle_Detail,Pending_Order,Delivery_Detail,Delivered_Order
import json
from django.urls import reverse
import json


class TestViews(TestCase):

    def setup(self):
        self.client = Client()
    
    def test_data(self):
        Vehicle_Class.objects.bulk_create([
            Vehicle_Class(vehicle_type='Bike', capacity=30, first_slot=True, second_slot=True, third_slot=True, fourth_slot=False),
            Vehicle_Class(vehicle_type='Scooty', capacity=50, first_slot=True, second_slot=True, third_slot=True, fourth_slot=False),
            Vehicle_Class(vehicle_type='Truck', capacity=100, first_slot=False, second_slot=True, third_slot=True, fourth_slot=True)
        ])

        vc1 = Vehicle_Class.objects.get(vehicle_type='Bike')
        vc2 = Vehicle_Class.objects.get(vehicle_type='Scooty')
        vc3 = Vehicle_Class.objects.get(vehicle_type='Truck')

        Vehicle_Detail.objects.bulk_create([
            Vehicle_Detail(registration_number="KA01AB1234",available=True,vehicle_class=vc1),
            Vehicle_Detail(registration_number="KA01AB1235",available=True,vehicle_class=vc1),
            Vehicle_Detail(registration_number="KA01AB1236",available=True,vehicle_class=vc1),
            Vehicle_Detail(registration_number="KA01AB1237",available=True,vehicle_class=vc2),
            Vehicle_Detail(registration_number="KA01AB1238",available=True,vehicle_class=vc2),
            Vehicle_Detail(registration_number="KA01AB1239",available=True,vehicle_class=vc3),
        ])

        Delivery_Partner.objects.bulk_create([
            Delivery_Partner(dl_number= "DL01382479",name= "Gopal1",contact= 7897129,email= "gopal1@grofers.com",available= True,two_wheeler= True,heavy_motor_vehicle= False),
            Delivery_Partner(dl_number= "DL01382480",name= "Gopal2",contact= 7897130,email= "gopal2@grofers.com",available= True,two_wheeler= True,heavy_motor_vehicle= False),
            Delivery_Partner(dl_number= "DL01382481",name= "Gopal3",contact= 7897131,email= "gopal3@grofers.com",available= True,two_wheeler= True,heavy_motor_vehicle= False),
            Delivery_Partner(dl_number= "DL01382482",name= "Gopal4",contact= 7897132,email= "gopal4@grofers.com",available= True,two_wheeler= True,heavy_motor_vehicle= False),
            Delivery_Partner(dl_number= "DL01382483",name= "Gopal5",contact= 7897133,email= "gopal5@grofers.com",available= True,two_wheeler= True,heavy_motor_vehicle= True),
        ])


    def test_project_list_post(self):
        TestViews.test_data(self)
        

        # vc1 = Vehicle_Class(vehicle_type='Bike', capacity=30, first_slot=True, second_slot=True, third_slot=True, fourth_slot=False)
        # vc1.save()
        # vc2 = Vehicle_Class(vehicle_type='Scooty', capacity=50, first_slot=True, second_slot=True, third_slot=True, fourth_slot=False)
        # vc2.save()
        # vc3 = Vehicle_Class(vehicle_type='Truck', capacity=100, first_slot=False, second_slot=True, third_slot=True, fourth_slot=True)
        # vc3.save()

        # vd1 = Vehicle_Detail(registration_number="KA01AB1234",available=True,vehicle_class=vc1)
        # vd1.save()
        # vd2 = Vehicle_Detail(registration_number="KA01AB1235",available=True,vehicle_class=vc1)
        # vd2.save()
        # vd3 = Vehicle_Detail(registration_number="KA01AB1236",available=True,vehicle_class=vc1)
        # vd3.save()
        # vd4 = Vehicle_Detail(registration_number="KA01AB1237",available=True,vehicle_class=vc2)
        # vd4.save()
        # vd5 = Vehicle_Detail(registration_number="KA01AB1238",available=True,vehicle_class=vc2)
        # vd5.save()
        # vd6 = Vehicle_Detail(registration_number="KA01AB1239",available=True,vehicle_class=vc3)
        # vd6.save()

        # dp1 = Delivery_Partner(dl_number= "DL01382479",name= "Gopal1",contact= 7897129,email= "gopal1@grofers.com",available= True,two_wheeler= True,heavy_motor_vehicle= False)
        # dp1.save()
        # dp2 = Delivery_Partner(dl_number= "DL01382480",name= "Gopal2",contact= 7897130,email= "gopal2@grofers.com",available= True,two_wheeler= True,heavy_motor_vehicle= False)
        # dp2.save()
        # dp3 = Delivery_Partner(dl_number= "DL01382481",name= "Gopal3",contact= 7897131,email= "gopal3@grofers.com",available= True,two_wheeler= True,heavy_motor_vehicle= False)
        # dp3.save()
        # dp4 = Delivery_Partner(dl_number= "DL01382482",name= "Gopal4",contact= 7897132,email= "gopal4@grofers.com",available= True,two_wheeler= True,heavy_motor_vehicle= False)
        # dp4.save()
        # dp5 = Delivery_Partner(dl_number= "DL01382483",name= "Gopal5",contact= 7897133,email= "gopal5@grofers.com",available= True,two_wheeler= True,heavy_motor_vehicle= True)
        # dp5.save()

        
        data = [
                [
                    {
                        "order_id": 1,
                        "order_weight": 20
                    },
                    {
                        "order_id": 2,
                        "order_weight": 20
                    },
                    {
                        "order_id": 3,
                        "order_weight": 20
                    },
                    {
                        "order_id": 13,
                        "order_weight": 10
                    },
                    {
                        "order_id": 14,
                        "order_weight": 10
                    },
                    {
                        "order_id": 15,
                        "order_weight": 10
                    },
                    {
                        "order_id": 16,
                        "order_weight": 10
                    }
                ],
                [
                    {
                        "order_id": 4,
                        "order_weight": 10
                    },
                    {
                        "order_id": 5,
                        "order_weight": 10
                    },
                    {
                        "order_id": 6,
                        "order_weight": 5
                    }
                ],
                [
                ],
                [
                    {
                        "order_id": 10,
                        "order_weight": 30
                    },
                    {
                        "order_id": 11,
                        "order_weight": 10
                    },
                    {
                        "order_id": 12,
                        "order_weight": 20
                    }
                ]
            ]
        
        response = self.client.post(reverse('delivery_assignment'),data,content_type="application/json")

        data = response.json()["data"]
        
        # assert response code is 200
        self.assertEqual(response.status_code,200)

        # assert we received response for all 4 slots
        self.assertEqual(len(data),4)

        # slot1 assertions
        # two vehicles alloted as order weight = 100
        self.assertEqual(len(data[0]),2)

        # both vehicles are scooty
        self.assertEqual(data[0][0]["vehicle_type"],"scooty")
        self.assertEqual(data[0][1]["vehicle_type"],"scooty")

        # slot2 assertions
        # weight <=30 so only one bike is alloted
        self.assertEqual(len(data[1]),1)
        self.assertEqual(data[1][0]["vehicle_type"],"bike")

        # assert driver who drives two wheeler is assigned
        partners = Delivery_Partner.objects.filter(two_wheeler= True)
        correct_partner_assignment = False
        for partner in partners:
            correct_partner_assignment = correct_partner_assignment or partner.dl_number == data[1][0]["delivery_partner_id"]
        
        self.assertTrue(correct_partner_assignment)

        # slot3 assertions
        # assert there is no vehicle alloted in 3rd slot
        self.assertEqual(len(data[2]),0)

        # slot4 assertions
        # only one vehicle alloted
        self.assertEqual(len(data[3]),1)

        # assert vehicle is truck
        self.assertEqual(data[3][0]["vehicle_type"],"truck")

        # asset only partner who can drive HMV is alloted
        self.assertEqual(data[3][0]["delivery_partner_id"],'DL01382483')


