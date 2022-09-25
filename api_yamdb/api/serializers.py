
from .models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


class GetTokenSerializer(serializers.ModelSerializer):
    pass

class UserSerializer(serializers.ModelSerializer):
    
    def validate_password(self, value: str) -> str:
        """Захешировать пароль юзера."""
        return make_password(value)

    def create(self, validated_data):
        """Создать юзера и сохранить захешированный пароль в БД."""
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role'
        )


class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username', 'email'
        )