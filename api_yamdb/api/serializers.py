from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from Review.models import Category, Comment, Genre, Review, Title


class CategorySerializer(serializers.ModelSerializer):
    lookup_field = 'slug'

    class Meta:
        fields = ('name', 'slug',)
        model = Category
        # read_only_fields = ('is_active', 'is_staff')
        # extra_kwargs = {
        #     'security_question': {'write_only': True},
        #     'security_question_answer': {'write_only': True},
        #     'password': {'write_only': True}
        # }


class GenreSerializer(serializers.ModelSerializer):
    lookup_field = 'slug'

    class Meta:
        fields = ('name', 'slug',)
        model = Genre


class TitlesSerializer(serializers.ModelSerializer):
    category = SlugRelatedField(slug_field='slug', read_only=True)
    genre = SlugRelatedField(slug_field='slug', read_only=True)

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
