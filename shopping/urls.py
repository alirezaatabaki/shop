from django.urls import path, re_path
from . import views


app_name = 'shopping'
urlpatterns = [
	path('', views.home, name='home'),
	re_path(r'category/(?P<slug>[-\w]+)/', views.home, name='category_filter'),
	re_path(r'detail/(?P<slug>[-\w]+)/', views.product_detail, name='product_detail'),
]