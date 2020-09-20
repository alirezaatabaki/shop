from rest_framework import serializers

from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['name', 'image', 'description', 'price', 'available', 'quantity']