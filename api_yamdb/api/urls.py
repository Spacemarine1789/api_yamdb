from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, SignUpView, GetTokenView

v1_router = DefaultRouter()

# Подключаем модель users к роутеру
v1_router.register('users', UserViewSet)

urlpatterns = [
    path('v1/auth/signup/', SignUpView.as_view(), name='sign_up'),
    path('v1/auth/token/', GetTokenView.as_view(), name='get_token'),
    path('v1/', include(v1_router.urls)),
]