from users.models import CustomUser
from rest_framework import serializers, permissions
from rest_framework.validators import UniqueValidator


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    confirmation_code = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = ('username', 'confirmation_code')


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('username', 'email',)

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                'Выберите другой логин.'
            )
        return value


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.is_admin or request.user.is_superuser)


class AdminUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role',
        )


class UserSerializer(serializers.ModelSerializer):
    role = serializers.StringRelatedField(read_only=True)
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=CustomUser.objects.all())
                    ], required=True,)
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=CustomUser.objects.all())
                    ],
    )

    class Meta:
        model = CustomUser
        fields = ('__all__')
