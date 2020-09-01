from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem, Coupon
from cart.cart_session import Cart
from suds.client import Client
from django.http import HttpResponse
from django.contrib import messages
from .forms import CouponForm
from django.views.decorators.http import require_POST
from django.utils import timezone


@login_required
def order_finalize(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    form = CouponForm()
    context = {
        'order': order,
        'form': form
    }
    return render(request, 'orders/order.html', context=context)


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    context = {
        'order': order,
    }
    return render(request, 'orders/order_detail.html', context=context)


@login_required
def order_list(request):
    orders = request.user.orders.all()
    context = {
        'orders': orders,
    }
    return render(request, 'orders/order_list.html', context=context)


@login_required
def order_create(request):
    cart = Cart(request)
    order = Order.objects.create(user=request.user)
    for item in cart:
        OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
    cart.clear()
    return redirect('orders:order-finalize', order.id)


# MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
# client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
# description = "پرداخت فروشگاه آنلاین"
# mobile = '09123456789'
# CallbackURL = 'http://localhost:8000/orders/verify/'


@login_required
def payment(request, order_id, price):
    global amount, o_id
    amount = price
    o_id = order_id
    result = request.GET.get('Status')
    response = redirect('orders:order-verify')
    response['Location'] += f'?Status={result}'
    return response
    # result = client.service.PaymentRequest(MERCHANT, amount, description, request.user.email, mobile, CallbackURL)
    # result = client.service.PaymentRequest(MERCHANT, amount, description, request.user.email, mobile, CallbackURL)
    # if result.Status == 100:
    #     return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
    # else:
    #     return HttpResponse('Error code: ' + str(result.Status))


@login_required
def verify(request):
    print(request.GET)
    if request.GET.get('Status') == 'OK':
        # result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
        # if result.Status == 100:
        order = Order.objects.get(id=o_id)
        order.paid = True
        order.save()
        messages.success(request, 'تراکنش با موفقیت انجام شد', 'success')
        return redirect('shopping:home')
        # elif result.Status == 101:
        #     return HttpResponse('Transaction submitted')
        # else:
        #     return HttpResponse('تراکنش ناموفق بود')
    else:
        messages.error(request, 'تراکنش ناموفق بود یا توسط کاربر لغو شد', 'danger')
        return redirect('shopping:home')


@require_POST
def coupon_apply(request, order_id):
    now = timezone.now()
    form = CouponForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(code__exact=code, valid_from__lte=now, valid_to__gte=now, active=True)
        except Coupon.DoesNotExist:
            messages.error(request, 'کد تخفیف یافت نشد', 'danger')
            return redirect('orders:order-finalize', order_id)
        order = Order.objects.get(id=order_id)
        order.discount = coupon.discount
        order.save()
    return redirect('orders:order-finalize', order_id)
