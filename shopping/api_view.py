from rest_framework.viewsets import ModelViewSet,ViewSet

from .models import Category,Product
from .serializers import CategorySerializer,ProductListSerializer

class CategoryListViewSet(ModelViewSet):
    queryset = Category.objects.all().filter(is_sub=False)
    serializer_class = CategorySerializer
    http_method_names = ['get']

class ProductListViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
