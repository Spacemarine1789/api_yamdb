from rest_framework import serializers

from Review.models import Category, Genre, Title


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