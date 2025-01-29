from django.urls import path
from .views import *

urlpatterns = [
    
    path('add/customer/',AddCustomerPage,name='url_addcustomer'),
    path('all/customer/',AllCustomer, name='url_allcustomer'),
    path('customer/delete/<int:id>/',DeleteCustomer,name='url_customer_delete'),
    path('customer/update/<int:id>/',UpdateCustomer,name='url_customer_update'),
    path('add/orders/', OrdersAdd),
    
]
