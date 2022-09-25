from rest_framework import viewsets, permissions

from Review.models import Category, Genre, Title
from .permissions import IsAdminOrReadOnly
from .serializers import CategorySerializer, GenreSerializer, TitlesSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    lookup_field = 'slug'
    serializer_class = CategorySerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly,)


class GenriesViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    lookup_field = 'slug'
    serializer_class = GenreSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly,)


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitlesSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly,)
