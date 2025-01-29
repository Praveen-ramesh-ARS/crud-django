from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductsView.as_view()),
    path('category/', CategoryView.as_view()),
    path('products/<int:id>/',Productget.as_view()),

    
    ]