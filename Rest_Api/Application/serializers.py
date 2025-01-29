from rest_framework import serializers
from .models import *

class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Product
        fields = "__all__"


class Selected_Serializer(serializers.ModelSerializer):

    class Meta:
        
        model = Product
        fields = ["product_name","product_code"]

class Category_Serializer(serializers.ModelSerializer):

    class Meta:
        
        model = Category
        fields = "__all__"
