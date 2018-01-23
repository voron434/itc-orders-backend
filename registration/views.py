import vk


def vk_auth(request):
    vk_token = request.GET.get('access_token')
    session = vk.Session()
    api = vk.API(session, v=5.0)
    user_info = api.users.get(access_token=vk_token)
