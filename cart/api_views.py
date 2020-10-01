from django.shortcuts import redirect
from requests import Response
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from cart.cart_session import Cart
from shopping.models import Product


@api_view(['GET', ])
def get_session_id(request):
    cart = Cart(request)
    cart.save()
    return Response({'session_id': cart.session.session_key})


@api_view(['GET', ])
def cart_detail(request):
    cart = Cart(request)
    return Response({**request.session, 'total': cart.get_total_price()})


@api_view(['POST', ])
def cart_add(request):
    cart = Cart(request)
    product = get_object_or_404(Product, id=request.data['product_id'])
    cart.add(product=product, quantity=request.data['quantity'])
    return Response({**request.session, 'total': cart.get_total_price()})


@api_view(['POST', ])
def cart_remove(request):
    cart = Cart(request)
    product = get_object_or_404(Product, id=request.data['product_id'])
    cart.remove(product)
    return Response({**request.session, 'total': cart.get_total_price()})
