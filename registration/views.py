from django.contrib.auth import authenticate, login
from django.http import JsonResponse

import vk
from vk.exceptions import VkAPIError

from .models import User
from .serializers import UserSerializer


def vk_auth(request):
    vk_token = request.GET.get('access_token')
    if vk_token:
        session = vk.Session()
        api = vk.API(session, v=5.0)
        try:
            user_info = api.users.get(access_token=vk_token, fields=['photo_200', ])[0]
        except VkAPIError as e:
            return JsonResponse({'error': {'code': e.code, 'message': e.message}})
        user_id = user_info['id']
        same_user = User.objects.filter(vk_id=user_id)
        if same_user.exists():
            user = authenticate(vk_id=user_id)
            login(request, user)
            json_user = UserSerializer(user)
            return JsonResponse({
                'success': True,
                'user': json_user.data
            })

        else:
            new_user = User(
                vk_id=user_id,
                first_name=user_info['first_name'],
                last_name=user_info['last_name'],
                role='User',
                picture=user_info['photo_200'],
            )
            new_user.save()
            user = authenticate(vk_id=user_id)
            login(request, user)
            json_user = UserSerializer(user)
            return JsonResponse({
                'success': True,
                'user': json_user.data
            })

    return JsonResponse({'error': True})
