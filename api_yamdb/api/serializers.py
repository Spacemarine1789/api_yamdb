
from .models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.validators import UniqueValidator


class GetTokenSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    confirmation_code = serializers.CharField()

    class Meta:
        model = User
        fields = (
            'username', 'confirmation_code'
        )

# class UserSerializer(serializers.ModelSerializer):
    
#     def validate_password(self, value: str) -> str:
#         """Захешировать пароль юзера."""
#         return make_password(value)

#     def create(self, validated_data):
#         """Создать юзера и сохранить захешированный пароль в БД."""
#         user = super().create(validated_data)
#         user.set_password(validated_data['password'])
#         user.save()
#         return user

#     class Meta:
#         model = User
#         fields = (
#             'username', 'email', 'first_name', 'last_name', 'bio', 'role'
#         )


class SignUpSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
        )
    email = serializers.EmailField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )

    def validate_username(self, value):
        if value.lower() == 'me':
            raise serializers.ValidationError('Username "me" is not valid')
        return value

    class Meta:
        model = User
        fields = (
            'username', 'email'
        )

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ],
        required=True,
    )
    email = serializers.EmailField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )

    class Meta:
        fields = ('username', 'email', 'first_name',
                  'last_name', 'bio', 'role')
        model = User


class UserEditSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('username', 'email', 'first_name',
                  'last_name', 'bio', 'role')
        model = User
        read_only_fields = ('role',)