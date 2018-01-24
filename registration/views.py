from django.contrib.auth import authenticate, login

import vk

from .models import User


def vk_auth(request):
    vk_token = request.GET.get('access_token')
    session = vk.Session()
    api = vk.API(session, v=5.0)
    user_info = api.users.get(access_token=vk_token, fields=['photo_200', ])[0]
    user_id = user_info['id']
    same_user = User.objects.filter(vk_id=user_id)
    if same_user.exists():
        user = authenticate(vk_id=user_id)
        login(request, user)
        return {'success': True}
    else:
        new_user = User(
            vk_id=user_id,
            first_name=user_info['first_name'],
            last_name=user_info['last_name'],
            role='User',
            picture=user_info['photo_200'],
        )
        new_user.save()
        return {'success': True}
    return {'error': True}
