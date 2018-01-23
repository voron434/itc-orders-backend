from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^auth$', views.vk_auth, name='vk_auth'),
]
