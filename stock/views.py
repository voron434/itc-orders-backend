from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from . import models
from . import serializers


@ensure_csrf_cookie
@login_required
def create_order(request):
    if request.POST:
        title = request.POST.get('title')
        description = request.POST.get('description')
        order = models.Order(
            title=title,
            description=description,
            orderer=request.user)
        order.save()
        return JsonResponse({'success': True})

    return JsonResponse({'error': True})


@login_required
def list_order(request):
    orders_list = models.Order.objects.filter(orderer=request.user)
    json_orders = serializers.OrderSerializer(orders_list, many=True)
    return JsonResponse({
        'success': True,
        'orders': json_orders,
    })
