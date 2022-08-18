
from .models import User
from api.serializers import TokenSerializer
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from api_yamdb.settings import DEFAULT_FROM_EMAIL


@api_view(['POST'])
@permission_classes([AllowAny])
def token(request):
    """Получаем токен"""
    serializer = TokenSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    username = serializer.data['username']
    user = get_object_or_404(User, username=username)
    confirmation_code = serializer.data['confirmation_code']
    if not default_token_generator.check_token(user, confirmation_code):
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    token = AccessToken.for_user(user)
    return Response(
        {'token': str(token)}, status=status.HTTP_200_OK
    )


def send_confirmation_code(user):
    """Отправка кода на почту"""
    confirmation_code = default_token_generator.make_token(user)
    subject = 'Код подтверждения на сервисе YaMDb'
    message = f'{confirmation_code} - ваш код авторизации на сервисе YaMDb'
    admin_email = DEFAULT_FROM_EMAIL
    user_email = [user.email]
    return send_mail(subject, message, admin_email, user_email)