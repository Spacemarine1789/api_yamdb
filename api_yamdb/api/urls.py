from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, CommentViewSet, GenriesViewSet, ReviewViewSet, TitlesViewSet

v1_router = DefaultRouter()
v1_router.register('categories', CategoryViewSet)
v1_router.register('genries', GenriesViewSet)
v1_router.register('titles', TitlesViewSet)
v1_router.register(
    r'titles/(?P<title_id>[\d]+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
v1_router.register(
    r'titles/(?P<title_id>[\d]+)/reviews/(?P<review_id>[\d]+)/comments',
    ReviewViewSet,
    basename='comments'
)


urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
