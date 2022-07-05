from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from .models import Author, Genre, Book, Application, IrvacApply, \
                    IrvacFullApply, Switter, Todo, Flat


class TodoSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'limit'
    max_page_size = 100


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        exclude = ('dt',)


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


class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flat
        fields = '__all__'
