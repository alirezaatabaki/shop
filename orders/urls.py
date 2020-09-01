from django.urls import path
from . import views

app_name = 'orders'
urlpatterns = [
    path('create/', views.order_create, name='order-create'),
    path('detail/<int:order_id>/', views.order_detail, name='order-detail'),
    path('list/', views.order_list, name='order-list'),
    path('<int:order_id>/', views.order_finalize, name='order-finalize'),
    path('payment/<int:order_id>/<price>/', views.payment, name='order-payment'),
    path('verify/', views.verify, name='order-verify'),
    path('apply/<int:order_id>/', views.coupon_apply, name='order-coupon-apply'),
]
