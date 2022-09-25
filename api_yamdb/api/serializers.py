from rest_framework import serializers

from Review.models import Category, Genre, Title


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Category
        extra_kwargs = {
            'name': {'required': True, 'max_length': 250},
            'slug': {'required': True, 'max_length': 50},
        }


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Genre
        extra_kwargs = {
            'name': {'required': True, 'max_length': 250},
            'slug': {'required': True, 'max_length': 50},
        }


class TitlesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Title
        extra_kwargs = {
            'name': {'required': True},
            'year': {'required': True},
            'description': {'required': False},
            'genre': {'required': True},
            'category': {'required': True},
        }
