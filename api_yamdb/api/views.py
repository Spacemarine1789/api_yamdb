from django.db.models import Avg
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from .permissions import IsAdminOrReadOnly, IsStaffOrAuthorOrReadOnly
from Review.models import Category, Genre, Title
from .serializers import (
    CategorySerializer, CommentSerializer, GenreSerializer,
    ReviewSerializer, TitlesSerializer
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    lookup_field = 'slug'


class GenriesViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminOrReadOnly,)
    lookup_field = 'slug'


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitlesSerializer
    permission_classes = (IsAdminOrReadOnly,)


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (IsStaffOrAuthorOrReadOnly,)

    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        reveiws = title.reviews.all()
        rating = reveiws.objects.annotate(Avg('score'))
        title.rating = round((rating[0].score__avg))

    def perform_update(self, serializer):
        serializer.save()
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        reveiws = title.reviews.all()
        rating = reveiws.objects.annotate(Avg('score'))
        title.rating = round((rating[0].score__avg))

    def perform_destroy(self, instance):
        instance.delete()
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        reveiws = title.reviews.all()
        rating = reveiws.objects.annotate(Avg('score'))
        title.rating = round((rating[0].score__avg))


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsStaffOrAuthorOrReadOnly,)

    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        review = get_object_or_404(
            title.reviews.all(), id=self.kwargs.get('review_id')
        )
        return review.сomments.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user
        )
