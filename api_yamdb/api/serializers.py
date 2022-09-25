from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from Review.models import Category, Comment, Genre, Review, Genre, Title

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Category


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Genre

class TitlesSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Title

class ReviewSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment
