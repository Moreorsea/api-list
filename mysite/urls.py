"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from blog.views import AuthorAPI, GenreAPI, BookAPI, ApplicationAPI, \
    IrvacApplyAPI, IrvacFullApplyAPI, SwitterAPI, TodoAPI, FlatAPI
from taskmanager.views import TaskAPI

router = routers.DefaultRouter()
router.register(r'author', AuthorAPI)
router.register(r'genre', GenreAPI)
router.register(r'book', BookAPI)
router.register(r'apply', ApplicationAPI)
router.register(r'apply-irvac', IrvacApplyAPI)
router.register(r'apply-irvac-full', IrvacFullApplyAPI)
router.register(r'posts', SwitterAPI)
router.register(r'todos', TodoAPI)
router.register(r'flat-list', FlatAPI)
router.register(r'tasks', TaskAPI)
router.register(r'task/<int:pk>', TaskAPI)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
