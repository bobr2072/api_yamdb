from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import token, register, UserViewSet


VERSION = 'v1'

router_v1 = DefaultRouter()
router_v1.register('users', UserViewSet, basename='users')

urlpatterns = [
    path(f'{VERSION}', include(router_v1.urls)),
    path(f'{VERSION}/auth/signup/', register, name='register'),
    path(f'{VERSION}/auth/token/', token, name='login'),
]
