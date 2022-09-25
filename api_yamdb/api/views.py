import datetime

from rest_framework import viewsets

from Review.models import Category, Genre, Title
from .permissions import IsAdminOrReadOnly
from .serializers import CategorySerializer, GenreSerializer, TitlesSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    lookup_field = 'slug'
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)


class GenriesViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    lookup_field = 'slug'
    serializer_class = GenreSerializer
    permission_classes = (IsAdminOrReadOnly,)


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitlesSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def validate(self, data):
        """
        Check that the current year is before entered year.
        """
        if data['year'] >= int(datetime.datetime.now().year):
            raise serializers.ValidationError("Введенная дата больше текущей")
        return data
