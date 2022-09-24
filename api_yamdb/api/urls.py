from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, GenriesViewSet, TitlesViewSet

v1_router = DefaultRouter()
v1_router.register('categories', CategoryViewSet)
v1_router.register('genries', GenriesViewSet)
v1_router.register('titles', TitlesViewSet)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
