import email
from email.message import EmailMessage
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignUpSerializer, UserSerializer, GetTokenSerializer, UserEditSerializer
from .models import User
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import action, api_view, permission_classes
from django.shortcuts import get_object_or_404
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.pagination import PageNumberPagination
from .permissions import (IsAdmin, IsAdminOrReadOnly,
                          IsAdminModeratorOwnerOrReadOnly)

# Create your views here.


# class SignUpView(APIView):
#     """
#     Получить код подтверждения на переданный email.
#     Права доступа: Доступно без токена.
#     Использовать имя 'me' в качестве username запрещено.
#     Поля email и username должны быть уникальными.
#     """

#     permission_classes = (permissions.AllowAny,)

#     @staticmethod
#     def send_email(data):
#         email = EmailMessage(
#             subject=data['email_subject'],
#             body=data['email_body'],
#             to=[data['to_email']]
#         )
#         email.send()
    
#     def post(self, request):
#         serializer = SignUpSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         email_body = (
#             f'Привет, {user.username}!'
#             '/nДля завершения регистрации укажите'
#             f'код-подтверждение: {user.confirmation_code}'
#         )
#         data = {
#             'email_body': email_body,
#             'to_email': user.email,
#             'email_subject': 'Код-подтверждение для доступа к API'
#         }
#         self.send_email(data)
#         return Response(serializer.data, status=status.HTTP_200_OK)


# class GetTokenView(APIView):
#     """
#     Получение JWT-токена в обмен на username и confirmation code.
#     Права доступа: Доступно без токена.
#     """

#     def post(self, request):
#         serializer = GetTokenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         data = serializer.validated_data
#         try:
#             user = User.objects.get(username=data['username'])
#         except User.DoesNotExist:
#             return Response(
#                 {
#                     'username': 'ПОльзователь не обнаружен'
#                 },
#                 status=status.HTTP_404_NOT_FOUND
#             )
#         if data.get('confirmation_code') == user.confirmation_code:
#             token = RefreshToken.for_user(user).access_token
#             return Response(
#                 {'token': str(token)},
#                 status=status.HTTP_201_CREATED
#             )
#         return Response(
#                 {'confirmation_code': 'Неверный код-подтверждение'},
#                 status=status.HTTP_400_BAD_REQUEST
#             )


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register(request):
    serializer = SignUpSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    user = get_object_or_404(
        User,
        username=serializer.validated_data['username']
    )
    confirmation_code = default_token_generator.make_token(user)
    send_mail(
        subject='YaMDb registration',
        message=f'Your confirmation code: {confirmation_code}',
        from_email=None,
        recipient_list=[user.email],
    )

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def get_jwt_token(request):
    serializer = GetTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = get_object_or_404(
        User,
        username=serializer.validated_data['username']
    )

    if default_token_generator.check_token(
        user, serializer.validated_data['confirmation_code']
    ):
        token = AccessToken.for_user(user)
        return Response({'token': str(token)}, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination
    permission_classes = (IsAdmin,)

    @action(
        methods=[
            'get',
            'patch',
        ],
        detail=False,
        url_path='me',
        permission_classes=[permissions.IsAuthenticated],
        serializer_class=UserEditSerializer,
    )
    def users_own_profile(self, request):
        user = request.user
        if request.method == 'GET':
            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        if request.method == 'PATCH':
            serializer = self.get_serializer(
                user,
                data=request.data,
                partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)