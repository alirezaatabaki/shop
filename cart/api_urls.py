from django.urls import path

from cart import api_views

urlpatterns = [
    path('session-id/', api_views.get_session_id, name='api-get-session-id'),
    path('detail/', api_views.cart_detail, name='api-cart-detail'),
    path('add/', api_views.cart_add, name='api-cart-add'),
    path('remove/', api_views.cart_remove, name='api-cart-remove')
]