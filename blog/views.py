from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AuthorSerializer, GenreSerializer, BookSerializer
from .models import Author, Genre, Book

# Create your views here.


class AuthorAPI(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class GenreAPI(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class BookAPI(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
