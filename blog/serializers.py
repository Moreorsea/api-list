from rest_framework import serializers
from .models import Author, Genre, Book, Application, IrvacApply, IrvacFullApply, Switter


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'


class IrvacApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = IrvacApply
        fields = '__all__'


class IrvacFullApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = IrvacFullApply
        fields = '__all__'


class SwitterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Switter
        fields = '__all__'
