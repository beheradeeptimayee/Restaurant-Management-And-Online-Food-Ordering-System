from django.urls import path
from orders.views import *

urlpatterns = [
    path('orders/', my_orders, name='orders'),
    path('checkout/', checkout, name='checkout'),
]
