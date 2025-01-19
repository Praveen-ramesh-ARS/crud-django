from django.urls import path
from .views import *

urlpatterns = [
    path('home/',HomePage),
    path('about/',AboutPage),
    path('contact/',ContactPage),
    path('services/',ServicesPage),
    path('addproducts/',AddProductsPage),
    path('products/',AllProducts),
    path('products/delete/<int:id>/',DeleteProducts,name='url_product_delete'),
    
]
