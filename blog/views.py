from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AuthorSerializer
from .models import Author

# Create your views here.


class AuthorAPI(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
