from django.urls import path,include
from django.conf.urls import url
from .views import delivery_assignment

urlpatterns = [
    # url to update models data
    url(r'^api/',include('delivery_app.api_urls')),

    #url to call delivery service for assignment
    url(r'^delivery',delivery_assignment,name="delivery_assignment"),
]