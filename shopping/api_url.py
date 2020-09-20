from rest_framework.routers import DefaultRouter

from .api_view import CategoryListViewSet, ProductListViewSet

router = DefaultRouter()
router.register('category',CategoryListViewSet)
router.register('products',ProductListViewSet)