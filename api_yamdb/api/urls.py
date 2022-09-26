from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, get_jwt_token, register

v1_router = DefaultRouter()

# Подключаем модель users к роутеру
v1_router.register(r'users', UserViewSet)

urlpatterns = [
    path('v1/auth/signup/', register, name='sign_up'),
    path('v1/auth/token/', get_jwt_token, name='get_token'),
    path('v1/', include(v1_router.urls)),
]