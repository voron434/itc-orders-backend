from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse

from . import models


@ensure_csrf_cookie
def create_order(request):
    if request.POST:
        title = request.POST.get('title')
        description = request.POST.get('description')
        order = models.Order(
            title=title,
            description=description,
            orderer=request.User)
        order.save()
        return JsonResponse({'success': True})

    return JsonResponse({'error': True})
