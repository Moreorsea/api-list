# import git
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from .filters import FlatFilter
from .serializers import AuthorSerializer, GenreSerializer, BookSerializer, \
    ApplicationSerializer, IrvacApplySerializer, \
    IrvacFullApplySerializer, SwitterSerializer, TodoSerializer, \
    TodoSetPagination, FlatSerializer
from .models import Author, Genre, Book, Application, IrvacApply, \
    IrvacFullApply, Switter, Todo, Flat


@csrf_exempt
def update(request):
    if request.method == "POST":
        '''
        pass the path of the diectory where your project will be
        stored on PythonAnywhere in the git.Repo() as parameter.
        Here the name of my directory is "test.pythonanywhere.com"
        '''
        repo = git.Repo("moreorsea.pythonanywhere.com/")
        origin = repo.remotes.origin

        origin.pull()

        return HttpResponse("Updated code on PythonAnywhere")
    else:
        return HttpResponse("Couldn't update the code on PythonAnywhere")


class TodoAPI(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = TodoSetPagination


class AuthorAPI(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class GenreAPI(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class BookAPI(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ApplicationAPI(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class IrvacApplyAPI(viewsets.ModelViewSet):
    queryset = IrvacApply.objects.all()
    serializer_class = IrvacApplySerializer


class IrvacFullApplyAPI(viewsets.ModelViewSet):
    queryset = IrvacFullApply.objects.all()
    serializer_class = IrvacFullApplySerializer


class SwitterAPI(viewsets.ModelViewSet):
    queryset = Switter.objects.all()
    serializer_class = SwitterSerializer


class FlatAPI(viewsets.ModelViewSet):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer
    filterset_class = FlatFilter
