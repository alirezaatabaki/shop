from rest_framework import serializers

from .models import Category, Product

class SubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name','id']

class CategorySerializer(serializers.ModelSerializer):
    sub_category = serializers.SerializerMethodField()
    def get_sub_category(self,instance):
        return SubSerializer(instance.subcategory.all(),many=True).data


    class Meta:
        model = Category
        fields = ['is_sub', 'name', 'sub_category']


class ProductListSerializer(serializers.ModelSerializer):
    category = SubSerializer(many=True)

    class Meta:
        model = Product
        fields = ['name', 'image', 'description', 'price', 'available', 'quantity','category']